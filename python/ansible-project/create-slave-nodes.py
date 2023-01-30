import boto3

ansible_master_node_pub_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDCTUNjEUwnIgJ0RmgVLeRFTYsTo5Z4TLPJANWZp61tJ1f4UK/YDH3HGQA8YSK6gv7ebO+G2u1XMLrEnHCD9Zj3HO7R3NB0rcCnTjhcobpNigeQ5BAJI2U7ueoCqwQFX8d26m5ycM2PVoGkWF87kX+N1I3If7nduMFRe2o6URRx5dJQv2I+31wh/TyHWB5tYwXRgelg4cQEPouNwQZklXl+SdrSVttTik64GYLqgS/wBz6XbBDCSUgvkNUGQpbOxH2otskrIuNZLQt5De4xovn8slgUCnjr5stJC3q/OXrEndXbMKaF5q553UKBUN1cF1b0Lqg20y6C2pgK1jMKFWAw6e28fOI/Op//4MBAfp689FuQ2ZlL2TTdENEIUj1PDRsVmORgAB5AH9pAFPghyQpbI32ewtg+oSapEeBKxpfNbxEO6EuqP4doX33wg2LXnwrUR5+Bw1kobzIXoi+UsxWGQhySvIYf8hA2SeX5dt9//tda1UzqaSD9Lf/aXJBY7m0= ubuntu@ip-172-31-56-57
"""
set_ssh_connection = """
# add ssh public key of manage node to authorized_keys

echo "%s" >> ~/.ssh/authorized_keys
""" % ansible_master_node_pub_key



def create_new_ec2(ami_id, min_count, max_count, instance_type, key_per_name, subnet_id, group_id, script):
    ec2 = boto3.resource("ec2")
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=min_count,
        MaxCount=max_count,
        InstanceType=instance_type,
        KeyName=key_per_name,
        NetworkInterfaces=[{
            'SubnetId': subnet_id,
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True,
            'Groups': [group_id]
        }],
        UserData=script
    )
    for instance in instances:
        instance.wait_until_running()
    return instances


def add_tag(instance, key, value):
    instance.create_tags(Tags=[{"Key": key, "Value": value}])


def set_srv_tags(instance, key_list, value_list):
    for n in range(len(key_list)):
        add_tag(instance, key_list[n], value_list[n])


