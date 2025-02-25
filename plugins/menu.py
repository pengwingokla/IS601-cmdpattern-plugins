# plugins/menu.py
from app.commands.command_handler import Command

class MenuCommand(Command):
    def execute(self, *args):
        return (
            "Available commands:\n"
            "- add <num1> <num2>: Add two numbers.\n"
            "- subtract <num1> <num2>: Subtract the second number from the first.\n"
            "- multiply <num1> <num2>: Multiply two numbers.\n"
            "- divide <num1> <num2>: Divide the first number by the second.\n"
            "- greet: Display a greeting message.\n"
            "- goodbye: Display a goodbye message.\n"
            "- discord <message>: Simulate sending a message to Discord.\n"
            "- menu: Display this menu.\n"
            "- exit: Exit the application."
        )

def register(handler):
    """Register the 'menu' command."""
    handler.register_command("menu", MenuCommand())