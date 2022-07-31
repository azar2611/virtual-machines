from datetime import datetime
import click
import json

@click.command()
@click.option("-t", "--type", required=True, help="How many core you need for e.g type1.large = 1 core, type.large = 2 core etc")
@click.option("-n", "--instancename", required=True, help="OS you want ubunut/centos/redhat")
@click.option("-im", "--imageid", required=True, help="OS you want ubunut/centos/redhat")
@click.option("-i", "--instanceid", required=True, help="OS you want ubunut/centos/redhat")
@click.option("-ip", "--ipaddress", required=True, help="OS you want ubunut/centos/redhat")



def cli(instancename, instanceid, imageid, type, ipaddress):

    """Start virtual machine (--type and --os required check help)"""
    vm = {
            "ImageId": imageid,
            "InstanceId": instanceid,
            "InstanceType": {
                "type": type,
                "CPU": "5",
                "os": ""
            },
            "KeyName": "ssh-key",
            "LaunchTime": "00/00/00 00:00:00",
            "Placement": {
                "AvailabilityZone": "us-west-2a"
            },
            "PrivateIpAddress": ipaddress,
            "State": {
                "Name": "stopped"
            },
            "SubnetId": "subnet-12345678910",
            "VpcId": "vpc-12345678910",
            "Architecture": "arm64",
            "Hypervisor": "xen",
            "RootDeviceName": "/dev/sda1",
            "RootDeviceType": "ebs",
            "RootDeviceSize": "100GB",
            "SecurityGroups": [
                {
                    "GroupName": "test-security-group",
                    "GroupId": "sg-12345678910"
                }
            ],
            "Tags": {
                "Key": "Name",
                "Value": instancename
            }
        }

    with open('virtual_machines.json','r+') as f:
        data = json.load(f)
        data["Instances"].append(vm)
        f.seek(0)
        json.dump(data, f, indent = 4)