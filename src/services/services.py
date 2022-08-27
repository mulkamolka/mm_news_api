from uuid import uuid4
from typing import Iterator

from src.repository.repositories import UserRepository
from src.domain.models import User


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()
