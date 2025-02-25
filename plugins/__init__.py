# plugins/__init__.py
import os
import importlib

def register_plugins(handler):
    """Register all plugins with the handler."""
    plugin_dir = "plugins"
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove '.py'
            module = importlib.import_module(f"{plugin_dir}.{module_name}")
            if hasattr(module, "register"):
                module.register(handler)