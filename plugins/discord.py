# plugins/discord.py
from app.commands.command_handler import Command

class DiscordCommand(Command):
    def execute(self, *args):
        """Execute the discord command."""
        if not args:
            return "Error: Please provide a message to send to Discord."
        message = " ".join(args)
        return f"Message sent to Discord: {message}"

def register(handler):
    """Register the 'discord' command with the handler."""
    handler.register_command("discord", DiscordCommand())