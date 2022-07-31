import os
import click

class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__("vm.commands.cmd_{}".format(name), None, None, ["cli"])
        except ImportError:
            return
        return mod.cli

cli = ComplexCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')
@click.command(cls=ComplexCLI)

def cli():
    """WELCOME TO THE VIRTUAL MACHINE CLI TOOL!!!"""
    pass

    