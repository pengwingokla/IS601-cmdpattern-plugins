# plugins/add.py
from app.commands.command_handler import Command

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Add command requires exactly 2 arguments.")
        return args[0] + args[1]

def register(handler):
    """Register the 'add' command."""
    handler.register_command("add", AddCommand())