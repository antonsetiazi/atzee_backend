# business/transactions/reference_generators/registry.py

class TransactionReferenceRegistry:

    _registry = {}

    @classmethod
    def register(cls, transaction_type, generator_func):
        cls._registry[transaction_type] = generator_func

    @classmethod
    def get_generator(cls, transaction_type):
        return cls._registry.get(transaction_type)