# core/users/seed_registry.py

USER_SEED_REGISTRY = []


def register_user_seed(data: dict):
    USER_SEED_REGISTRY.append(data)


def all_user_seeds():
    return USER_SEED_REGISTRY


def reset_registry():
    USER_SEED_REGISTRY.clear()