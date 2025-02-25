import pytest
from app.commands.core import Application 
from app.commands.command_handler import CommandHandler 

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = Application()
    app.start()
    out, err = capfd.readouterr()

    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Welcome to the application. Type 'menu' for a list of commands." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Application()
    app.start()
    out, err = capfd.readouterr()

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Welcome to the application. Type 'menu' for a list of commands." in out
    assert "Unknown command: unknown_command" in out
    assert "Exiting..." in out

def test_app_menu_command(capfd, monkeypatch):
    """Test that the 'menu' command displays the list of available commands."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Application()
    app.start()
    out, err = capfd.readouterr()

    # Check that the menu is displayed
    assert "Available commands:" in out
    assert "- add <num1> <num2>: Add two numbers." in out
    assert "- subtract <num1> <num2>: Subtract the second number from the first." in out
    assert "- multiply <num1> <num2>: Multiply two numbers." in out
    assert "- divide <num1> <num2>: Divide the first number by the second." in out
    assert "- greet: Display a greeting message." in out
    assert "- goodbye: Display a goodbye message." in out
    assert "- discord <message>: Simulate sending a message to Discord." in out
    assert "- menu: Display this menu." in out
    assert "- exit: Exit the application." in out
    assert "Exiting..." in out

def test_app_add_command(capfd, monkeypatch):
    """Test that the 'add' command works correctly."""
    # Simulate user entering 'add 2 3' followed by 'exit'
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Application()
    app.start()
    out, err = capfd.readouterr()

    # Check that the result of the addition is displayed
    assert "Result: 5.0" in out
    assert "Exiting..." in out

def test_app_divide_by_zero(capfd, monkeypatch):
    """Test that the 'divide' command handles division by zero correctly."""
    # Simulate user entering 'divide 10 0' followed by 'exit'
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Application()
    app.start()
    out, err = capfd.readouterr()

    # Check that the division by zero error is handled
    assert "Error: Cannot divide by zero." in out
    assert "Exiting..." in out