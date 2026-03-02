# business/transactions/policies/registry.py

class TransactionPolicyRegistry:

    _policies = []

    @classmethod
    def register(cls, policy):
        cls._policies.append(policy)

    @classmethod
    def get_policies(cls):
        return cls._policies