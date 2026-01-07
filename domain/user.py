from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id: int, username: str, role):
        self.user_id = user_id
        self.username = username
        self._role = role

    @abstractmethod
    def can_access(self, permission) -> bool:
        pass