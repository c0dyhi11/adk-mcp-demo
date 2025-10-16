"""This module auto-discovers and imports all tool packages in the tools directory."""
import pkgutil
import importlib

for importer, modname, ispkg in pkgutil.walk_packages(path=__path__,
                                                      prefix=__name__+'.',
                                                      onerror=lambda x: None):
    if ispkg:
        try:
            importlib.import_module(modname)
            print(f"Discovered and loaded tool package: {modname}")
        except Exception as e:
            print(f"Failed to load package {modname}: {e}")
