# app/commands/command_handler.py
from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        """Execute the command with the given arguments."""
        pass

# Command Handler
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Register a command with the handler."""
        self.commands[name] = command

    def execute_command(self, name, *args):
        """Execute a registered command."""
        if name in self.commands:
            return self.commands[name].execute(*args)
        else:
            raise ValueError(f"Unknown command: {name}")