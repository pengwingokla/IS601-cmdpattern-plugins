# app/commands/core.py
from app.commands.command_handler import CommandHandler
from plugins import register_plugins  # Import plugins from the plugins directory

class Application:
    def __init__(self):
        self.handler = CommandHandler()
        register_plugins(self.handler)  # Register plugins

    def start(self):
        """Start the REPL."""
        print("Welcome to the application. Type 'menu' for a list of commands.")
        while True:
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                print("Exiting...")
                break

            parts = user_input.split()
            if not parts:
                continue

            command_name = parts[0]
            args = parts[1:]

            try:
                # Convert arguments to floats for calculator commands
                if command_name in ["add", "subtract", "multiply", "divide"]:
                    args = list(map(float, args))
                result = self.handler.execute_command(command_name, *args)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")