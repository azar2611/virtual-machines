from tabnanny import verbose
import click
import json

@click.command()

def cli():
    f = open('virtual_machines.json')
    data = json.load(f)
    for instance in data['Instances']:
        print(instance['ImageId'])
    