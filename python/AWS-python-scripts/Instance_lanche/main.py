import boto3


def create_new_ec2(ami_id, min_count, max_count, instance_type, key_per_name):
    ec2 = boto3.resource("ec2")
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=min_count,
        MaxCount=max_count,
        InstanceType=instance_type,
        KeyName=key_per_name
    )


