# business/payment_gateway/providers/base.py

from abc import ABC, abstractmethod


class BasePaymentProvider(ABC):
    """
    Abstract base class for all payment providers.
    """

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def create_payment(self, payment):
        """
        Create payment to external gateway.
        Must return standardized response.
        """
        raise NotImplementedError

    @abstractmethod
    def parse_webhook(self, payload: dict) -> dict:
        """
        Normalize webhook payload.
        """
        raise NotImplementedError