from datetime import datetime
import click
import json
import logging

@click.command()
@click.option("-t", "--type", required=True, help="How many core you need for e.g type1.large = 1 core, type.large = 2 core etc")
@click.option("-n", "--instancename", required=True, help="Instance Name e.g instance10")
@click.option("-im", "--imageid", required=True, help="Image id for e.g img-12345678910")
@click.option("-i", "--instanceid", required=True, help="Instance id for e.g i-12345678910")
@click.option("-ip", "--ipaddress", required=True, help="IP address of machine for e.g 10.10.10.12")



def cli(instancename, instanceid, imageid, type, ipaddress):

    """Add virtual machine (--type, --instancename, imageid, instanceid, ipaddress required check help)"""
    #vm json block
    vm = {
            "ImageId": imageid,
            "InstanceId": instanceid,
            "InstanceType": {
                "type": type,
                "CPU": type.split('.')[0][-1],
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

    try:
        with open('virtual_machines.json','r+') as f:
            data = json.load(f)
            
            #collect all instance ids 
            vms = [None] * len(data["Instances"])
            for instance in data["Instances"]:
                vms.append(instance['InstanceId'])

            if instanceid not in vms:    
                #Add new vm
                data["Instances"].append(vm)
                f.seek(0)
                json.dump(data, f, indent = 4)
                
                click.echo("You have added Virtual Machine")
                click.echo("Name::{}, IP Address::{}, Type::{}".format(instancename, ipaddress, type))

            else:
                click.echo("Instance ID {} already present please provide unique ID".format(instanceid))

    except FileNotFoundError:
        logging.error("File does not exixts")

    
    