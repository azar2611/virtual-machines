import click
import json
import logging

@click.command()
@click.option("-r", "--running", help="List all Running Virtual Machines.") 
@click.option("-s", "--stopped", help="List all Stopped Virtual Machines.")

def cli(running, stopped):
    """Default list all vms (Try --running=yes /--stopped=yes)"""
    
    try:
        with open('virtual_machines.json','r+') as f:
            data = json.load(f)

        click.echo("------------------------------------------------------------------------------------------------------------------------------------")
        click.echo("Name\t\tInstance ID\tImage ID\t  Instance state  Instance type\t  Private IP\tAvailanility Zone  Launch time")
        click.echo("------------------------------------------------------------------------------------------------------------------------------------")

        for instance in data['Instances']:
            if running == 'yes' and instance['State']['Name'] == 'running':
                #Print only running instances.
                print("{}\t{}\t{}\t  {}\t  {}\t  {}\t{}\t   {}".format(instance['Tags']['Value'],instance['InstanceId'], \
                     instance['ImageId'],instance['State']['Name'],instance['InstanceType']['type'],instance['PrivateIpAddress'],\
                     instance['Placement']['AvailabilityZone'],instance['LaunchTime']))

            elif stopped == 'yes' and instance['State']['Name'] == 'stopped':
                #Print only stopped instances.
                print("{}\t{}\t{}\t  {}\t  {}\t  {}\t{}\t   {}".format(instance['Tags']['Value'],instance['InstanceId'], \
                     instance['ImageId'],instance['State']['Name'],instance['InstanceType']['type'],instance['PrivateIpAddress'],\
                     instance['Placement']['AvailabilityZone'],instance['LaunchTime']))

            elif running == None and stopped == None:
                #Print all instances.
                print("{}\t{}\t{}\t  {}\t  {}\t  {}\t{}\t   {}".format(instance['Tags']['Value'],instance['InstanceId'], \
                     instance['ImageId'],instance['State']['Name'],instance['InstanceType']['type'],instance['PrivateIpAddress'],\
                     instance['Placement']['AvailabilityZone'],instance['LaunchTime']))

    except FileNotFoundError:
        logging.error("File does not exixts")