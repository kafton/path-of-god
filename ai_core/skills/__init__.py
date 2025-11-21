# ai_core/skills/__init__.py
# This file intentionally left simple. It will expose skill modules present.
# Dynamic import helper (safe).
import importlib
import pkgutil

__all__ = []

# auto-populate __all__ based on present .py files (excluding __init__)
for finder, name, ispkg in pkgutil.iter_modules(__path__):
    if name != "__init__":
        __all__.append(name)
