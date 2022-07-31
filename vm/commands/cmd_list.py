import click
import json

@click.command()
@click.option("-r", "--running", help="List all Running Virtual Machines.")
@click.option("-s", "--stopped", help="List all Stopped Virtual Machines.")

def cli(running, stopped):
    """Default list all vms (Try --running=yes /--stopped=yes)"""
    f = open('virtual_machines.json')
    data = json.load(f)
    click.echo("------------------------------------------------------------------------------------------------------------------------------------")
    click.echo("Name\t\tInstance ID\tImage ID\t  Instance state  Instance type\t  Private IP\tAvailanility Zone  Launch time")
    click.echo("------------------------------------------------------------------------------------------------------------------------------------")
    for instance in data['Instances']:
        if running == 'yes' and instance['State']['Name'] == 'running':
            print("{}\t{}\t{}\t  {}\t  {}\t  {}\t{}\t   {}".format(instance['Tags']['Value'],instance['InstanceId'], instance['ImageId'],instance['State']['Name'],instance['InstanceType']['type'],instance['PrivateIpAddress'],instance['Placement']['AvailabilityZone'],instance['LaunchTime']))
        elif stopped == 'yes' and instance['State']['Name'] == 'stopped':
            print("{}\t{}\t{}\t  {}\t  {}\t  {}\t{}\t   {}".format(instance['Tags']['Value'],instance['InstanceId'], instance['ImageId'],instance['State']['Name'],instance['InstanceType']['type'],instance['PrivateIpAddress'],instance['Placement']['AvailabilityZone'],instance['LaunchTime']))
        elif running == None and stopped == None:
            print("{}\t{}\t{}\t  {}\t  {}\t  {}\t{}\t   {}".format(instance['Tags']['Value'],instance['InstanceId'], instance['ImageId'],instance['State']['Name'],instance['InstanceType']['type'],instance['PrivateIpAddress'],instance['Placement']['AvailabilityZone'],instance['LaunchTime']))