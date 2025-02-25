# plugins/greet.py
from app.commands.command_handler import Command

class GreetCommand(Command):
    def execute(self, *args):
        """Execute the greet command."""
        return "Hello! Welcome to the application."

def register(handler):
    """Register the 'greet' command with the handler."""
    handler.register_command("greet", GreetCommand())