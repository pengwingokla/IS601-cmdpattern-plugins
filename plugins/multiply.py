# plugins/multiply.py
from app.commands.command_handler import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Multiply command requires exactly 2 arguments.")
        return args[0] * args[1]

def register(handler):
    """Register the 'multiply' command."""
    handler.register_command("multiply", MultiplyCommand())