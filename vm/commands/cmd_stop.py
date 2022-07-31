from datetime import datetime
import click
import json
import logging

@click.command()
@click.option("-i", "--instanceid", required=True, help="Instance ID for e.g i-12345678910")

def cli(instanceid):
    """Stop virtual machine (--instanceid required check help)"""

    match = None
    try:
        with open('virtual_machines.json','r+') as f:
            data = json.load(f)
    
            for instance in data['Instances']:
                if instance['InstanceId'] == instanceid:

                    match = True
                    #chnaged virtual machine state
                    instance['State']['Name'] = 'stopped'
                    instance['LaunchTime'] = '00/00/00 00:00:00'
    
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
    
                    click.echo("You have stopped Virtual Machine")
                    click.echo("Name::{}, IP Address::{}".format(instance['Tags']['Value'],instance['PrivateIpAddress']))
    
                    break
            if match != True:
                click.echo("Instance with id {} not found".format(instanceid))

    except FileNotFoundError:
        logging.error("File does not exixts")