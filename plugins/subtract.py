# plugins/subtract.py
from app.commands.command_handler import Command

class SubtractCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("Subtract command requires exactly 2 arguments.")
        return args[0] - args[1]

def register(handler):
    """Register the 'subtract' command."""
    handler.register_command("subtract", SubtractCommand())