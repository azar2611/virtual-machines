import click
import json

@click.command()
@click.option("-t", "--type", required=True, help="How many core you need for e.g type1.large = 1 core, type.large = 2 core etc")
@click.option("-i", "--instanceid", required=True, help="Instance id for e.g i-12345678910")


def cli(type, instanceid):

    """Modify virtual machine (Only --type modify  --instanceid required check help)"""    

    with open('virtual_machines.json','r+') as f:
        data = json.load(f)

        for instance in data['Instances']:
            if instance['InstanceId'] == instanceid:
                instance['InstanceType']['type'] = type

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

                click.echo("You have modified Virtual Machine")
                click.echo("Name::{}, Type::{}".format(instance['Tags']['Value'],instance['InstanceType']['type']))

                break