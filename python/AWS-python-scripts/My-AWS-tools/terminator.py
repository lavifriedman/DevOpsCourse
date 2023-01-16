import boto3
from datetime import datetime


def terminator(instances_id_list):
    ec2 = boto3.resource('ec2')
    # iterate through instance IDs and terminate them
    for id in instances_id_list:
        instance = ec2.Instance(id)
        instance.terminate()


def terminate_old_instance():
    old_date_instance =[]
    ec2 = boto3.client('ec2')
    for reservations in ec2.describe_instances()['Reservations']:
        for instance in reservations['Instances']:
            date_now = datetime.now()
            launch_datetime = instance['LaunchTime']
            date_now = int(date_now.strftime('%Y%m%d'))
            launch_datetime = int(launch_datetime.strftime('%Y%m%d'))
            if date_now - launch_datetime < 7:
                old_date_instance.append(instance["InstanceId"])
    terminator(old_date_instance)


def main():
    terminate_old_instance()


if __name__ == "__main__":
    terminate_old_instance()
