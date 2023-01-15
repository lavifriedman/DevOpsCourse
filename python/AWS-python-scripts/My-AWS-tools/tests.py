import boto3
import json


def runRemoteShellCommands (InstanceId, commands_script):
    ssm_client = boto3.client('ssm', region_name="us-east-1")
    response = ssm_client.send_command( InstanceIds=[InstanceId], DocumentName="AWS-RunShellScript", Parameters={'commands':commands_script},)
    command_id = response['Command']['CommandId']
    output = ssm_client.get_command_invocation( CommandId=command_id, InstanceId=InstanceId)
    while output['Status'] == "InProgress":
        output = ssm_client.get_command_invocation( CommandId=command_id, InstanceId=InstanceId)
    print(output['StandardOutputContent'])

instances_list = ["i-01e23eb7e016b9ce5", "i-0e01fcdda5440c5e6", "i-049e7e24e95750946", "i-081053e9f06409808"]
runRemoteShellCommands("i-01e23eb7e016b9ce5")