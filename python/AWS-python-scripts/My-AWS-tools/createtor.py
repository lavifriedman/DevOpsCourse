import boto3
import time
from datetime import datetime


def create_vpc(cidr_block, vpc_name=None, internet_gateway_id=None):
    """Function create a new VPC over AWS plat"""
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


def create_new_ec2(ami_id, min_count, max_count, instance_type, key_per_name, subnet_id, group_id, iam_role_name):
    ec2 = boto3.resource("ec2")
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=min_count,
        MaxCount=max_count,
        InstanceType=instance_type,
        KeyName=key_per_name,
        IamInstanceProfile= {'Name': iam_role_name},
        NetworkInterfaces=[{
            'SubnetId': subnet_id,
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True,
            'Groups': [group_id]
        }],
    )
    for instance in instances:
        instance.wait_until_running()
    return instances


def get_instance_name(instance):
    for tags in instance.tags:
        if tags["Key"] == 'Name':
            instance_name = tags["Value"]
    return instance_name


def save_instances_profile_in_file(instances, file_path):
    with open(file_path, "w") as file:
        for instance in instances:
            file.write('instance-type:{}\n'.format(instance.instance_type))
            file.write('key-name: {}\n'.format(get_instance_name(instance)))
            file.write('security-group: {}\n'.format(instance.security_groups))


def add_name_and_date_to_instances(instances):
    date_now = datetime.now()
    date_now = str(date_now.strftime('%d-%m-%Y'))
    count = 0
    for instance in instances:
        count += 1
        instance.create_tags(Tags=[{"Key": "Name", "Value": "web-srv-" + str(count)}])
        instance.create_tags(Tags=[{"Key": "Data", "Value": date_now}])


def print_instances_privet_ip(instances):
    for instance in instances:
        print(instance.private_ip_address)


def run_remote_shell_commands (instance_id, commands_script):
    ssm_client = boto3.client('ssm', region_name="us-east-1")
    response = ssm_client.send_command( InstanceIds=[instance_id], DocumentName="AWS-RunShellScript", Parameters={'commands':commands_script},)
    command_id = response['Command']['CommandId']
    time.sleep(2)
    output = ssm_client.get_command_invocation( CommandId=command_id, InstanceId=instance_id)
    while output['Status'] == "InProgress":
        output = ssm_client.get_command_invocation( CommandId=command_id, InstanceId=instance_id)


def script_convert_commands_list(file_path):
    with open(file_path, "r") as file_commands:
        commands_list = []
        for command in file_commands:
            commands_list.append(command.split("\n")[0])
    return commands_list


def set_apache_srv_over_instances(instdances, file_path1, file_path2):
    command_list1 = script_convert_commands_list(file_path1)
    command_list2 = script_convert_commands_list(file_path2)
    for instance in instdances:
        run_remote_shell_commands(instance.id, command_list1)
        run_remote_shell_commands(instance.id, command_list2)


def collect_instance_number_from_user():
    user_input = input("Enter please the number of instances you wish to launch: ")
    while True:
        try:
            return int(user_input)
        except ValueError:
            print("Your input is not legal, please check you enter a number.")


def main():
    Cidr_block = "192.168.10.0/24"
    subnet_block = "192.168.10.0/28"
    route_block = "0.0.0.0/0"
    ig_id = create_internet_gateway("new-ig")
    vpc = create_vpc(Cidr_block, "new-vpc", ig_id)
    subnet = create_subnet(vpc.id, subnet_block, "new-subnet")
    create_route_table(vpc, route_block, ig_id, subnet.id)
    sg = create_sg(vpc)
    instances_number = collect_instance_number_from_user()
    role_profile_name = input("Enter please the name of the role for set ssm IamInstanceProfile ")
    web_servers = create_new_ec2("ami-0b5eea76982371e91", instances_number, instances_number, "t3.micro", "ServerLXF01key", subnet.id, sg.id,
                                 role_profile_name)
    add_name_and_date_to_instances(web_servers)
    print_instances_privet_ip(web_servers)
    save_instances_profile_in_file(web_servers, "configuration")
    set_apache_srv_over_instances(web_servers, "set-apache-srv-part1", "set-apache-srv-part2")


if __name__ == "__main__":
    main()

