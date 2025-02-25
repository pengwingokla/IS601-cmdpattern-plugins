# app/commands/app.py
from .core import Application

if __name__ == "__main__":
    app = Application()
    app.start()