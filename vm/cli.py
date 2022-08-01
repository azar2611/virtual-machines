import os
import click

class ComplexCLI(click.MultiCommand):
    
    #list command by removinf cmd_ and .py
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))
        commands.sort()
        return commands
    #get commands
    def get_command(self, ctx, name):
        try:
            mod = __import__("vm.commands.cmd_{}".format(name), None, None, ["cli"])
        except ImportError:
            return
        return mod.cli

@click.command(cls=ComplexCLI)

def cli():
    """WELCOME TO THE VIRTUAL MACHINE CLI TOOL!!!"""
    pass

    