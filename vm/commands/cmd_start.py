from datetime import datetime
import click
import json

@click.command()
@click.option("-t", "--type", required=True, help="How many core you need for e.g type1.large = 1 core, type.large = 2 core etc")
@click.option("-o", "--os", required=True, help="OS you want ubunut/centos/redhat")

def cli(type, os):

    """Start virtual machine (--type and --os required check help)"""

    now = datetime.now()
    current_time = now.strftime("%D %H:%M:%S")
    print("Current Time =", current_time)

    with open('virtual_machines.json','r+') as f:
        data = json.load(f)

        for instance in data['Instances']:
            if instance['State']['Name'] == 'stopped':

                instance['State']['Name'] = 'running'
                instance['InstanceType']['type'] = type
                instance['InstanceType']['os'] = os

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

                click.echo("You have started Virtual Machine")
                click.echo("Name::{}, IP Address::{}, Type::{}, OS::{}".format(instance['Tags']['Value'],instance['PrivateIpAddress'],instance['InstanceType']['type'],instance['InstanceType']['os']))

                break

            
        click.echo("Virtual Machine NOT Available")

