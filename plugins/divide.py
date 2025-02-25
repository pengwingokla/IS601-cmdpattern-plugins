# plugins/divide.py
from app.commands.command_handler import Command

class DivideCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Divide command requires exactly 2 arguments.")
        if args[1] == 0:
            raise ValueError("Cannot divide by zero.")
        return args[0] / args[1]

def register(handler):
    """Register the 'divide' command."""
    handler.register_command("divide", DivideCommand())