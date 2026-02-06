# core/verticals/registry.py

VERTICALS = {}

def register_vertical(manifest):
    VERTICALS[manifest["key"]] = manifest
