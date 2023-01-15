import boto3
import json


def terminator(instances_id_list):
    ec2 = boto3.resource("ec2")
    ec2.instances.filter(InstanceIds=instances_id_list).terminate()


def create_vpc(cidr_block, vpc_name=None, internet_gateway_id=None):
    ec2 = boto3.resource("ec2")
    vpc = ec2.create_vpc(CidrBlock=cidr_block)
    if vpc_name is not None:
        vpc.create_tags(Tags=[{"Key": "Name", "Value": vpc_name}])
    if internet_gateway_id is not None:
        vpc.attach_internet_gateway(InternetGatewayId=internet_gateway_id)
    return vpc


def create_subnet(vpc_id, cidr_block, subnet_name=None):
    ec2 = boto3.resource("ec2")
    subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)
    if subnet_name is not None:
        subnet.create_tags(Tags=[{"Key": "Name", "Value": subnet_name}])
    return subnet


def create_route_table(vpc, cidr_block, internet_gateway_id, subnet_id=None):
    route_table = vpc.create_route_table()
    route = route_table.create_route(DestinationCidrBlock=cidr_block, GatewayId=internet_gateway_id)
    if subnet_id is not None:
        route_table.associate_with_subnet(SubnetId=subnet_id)


def create_internet_gateway(internet_gateway_name=None):
    ig = boto3.resource("ec2")
    internet_gateway = ig.create_internet_gateway()
    if internet_gateway_name is not None:
        internet_gateway.create_tags(Tags=[{"Key": "Name", "Value": internet_gateway_name}])
    return internet_gateway.id


def create_sg(vpc):
    ec2 = boto3.resource("ec2")
    sg = ec2.create_security_group(GroupName='Project-sg', Description='only allow SSH  and http traffic', VpcId=vpc.id)
    sg.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)
    sg.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=80, ToPort=80)
    return sg


def get_role_dic_for_instance(role_name):
    client = boto3.client('iam')
    role_profile = client.get_role(RoleName=role_name)
    return {'name': role_profile['Role']['Name']}


def create_new_ec2(ami_id, min_count, max_count, instance_type, key_per_name, subnet_id, sg, iam_rolue):
    ec2 = boto3.resource("ec2")
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=min_count,
        MaxCount=max_count,
        InstanceType=instance_type,
        KeyName=key_per_name,
        IamInstanceProfile= iam_rolue,
        NetworkInterfaces=[{
            'SubnetId': subnet_id,
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True,
            'Groups': [sg.group_id]
        }],
    )
    for instance in instances:
        instance.wait_until_running()
    return instances


def add_name_and_date_to_instances(instance):
    count = 0
    for instance in instance:
        count += 1
        instance.create_tags(Tags=[{"Key": "Name", "Value": "web-srv-" + str(count)}])
        instance.create_tags(Tags=[{"Key": "Data", "Value": "15.1.2023"}])


def print_instances_privet_ip(web_servers):
    for instance in web_servers:
        print(instance.private_ip_address)


def run_remote_shell_commands (InstanceId, commands_script):
    ssm_client = boto3.client('ssm', region_name="us-east-1")
    response = ssm_client.send_command( InstanceIds=[InstanceId], DocumentName="AWS-RunShellScript", Parameters={'commands':commands_script},)
    command_id = response['Command']['CommandId']
    output = ssm_client.get_command_invocation( CommandId=command_id, InstanceId=InstanceId)
    while output['Status'] == "InProgress":
        output = ssm_client.get_command_invocation( CommandId=command_id, InstanceId=InstanceId)
    print(output['StandardOutputContent'])

Cidr_block = "192.168.10.0/24"
subnet_block = "192.168.10.0/28"
route_block = "0.0.0.0/0"
ig_id = create_internet_gateway("new-ig")
vpc = create_vpc(Cidr_block, "new-vpc", ig_id)
subnet = create_subnet(vpc.id, subnet_block, "new-subnet")
create_route_table(vpc, route_block, ig_id, subnet.id)
sg = create_sg(vpc)
rolue_dic = get_role_dic_for_instance("ssm-rolue")
web_servers = create_new_ec2("ami-0b5eea76982371e91", 4, 4, "t3.micro", "ServerLXF01key", subnet.id, sg, {'Name': 'ssm-rolue'})
print(web_servers)
add_name_and_date_to_instances(web_servers)
print_instances_privet_ip(web_servers)
instance_ids = []
for instance in web_servers:
    instance_ids.append(instance.id)



