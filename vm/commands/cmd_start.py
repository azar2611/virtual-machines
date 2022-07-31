from datetime import datetime
import click
import json
import logging

@click.command()
@click.option("-t", "--type", required=True, help="How many core you need for e.g type1.large = 1 core, type.large = 2 core etc")
@click.option("-o", "--os", required=True, help="OS you want ubunut/centos/redhat")

def cli(type, os):

    """Start virtual machine (--type and --os required check help)"""

    no_running=None
    #Launch time of virtual machine
    now = datetime.now()
    current_time = now.strftime("%D %H:%M:%S")
    
    try:
        with open('virtual_machines.json','r+') as f:
            data = json.load(f)

            for instance in data['Instances']:
                if instance['State']['Name'] == 'stopped':

                    no_running = False

                    #Update virtual machine
                    instance['State']['Name'] = 'running'
                    instance['InstanceType']['type'] = type
                    instance['InstanceType']['os'] = os
                    instance['LaunchTime'] = current_time

                    f.seek(0)
                    #Dump to file
                    json.dump(data, f, indent=4)
                    f.truncate()

                    click.echo("You have started Virtual Machine")
                    click.echo("Name::{}, IP Address::{}, Type::{}, OS::{}".format(instance['Tags']['Value'],instance['PrivateIpAddress'],instance['InstanceType']['type'],instance['InstanceType']['os']))

                    break
                else:
                    no_running = True

            if no_running == True:
                click.echo("Virtual Machine NOT Available!!!")

    except FileNotFoundError:
        logging.error("File does not exixts")


