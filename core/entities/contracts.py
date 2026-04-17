# core/entities/contracts.py

from abc import ABC, abstractmethod

class BaseEntity(ABC):
    key: str
    permission: str

    @abstractmethod
    def query(self, *, user, tenant, query: dict) -> dict:
        raise NotImplementedError

