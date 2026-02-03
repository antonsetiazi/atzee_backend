# core/workflows/context.py

class WorkflowContext:
    """
    Shared context across workflow steps.
    """

    def __init__(self, *, tenant, user, transaction):
        self.tenant = tenant
        self.user = user
        self.transaction = transaction

        self.data: dict = {}
        self.logs: list[str] = []

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def log(self, message: str):
        self.logs.append(message)
