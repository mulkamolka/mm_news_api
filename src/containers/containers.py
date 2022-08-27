"""Containers module."""
import os
from dependency_injector import containers, providers

from src.database.database import Database
from src.repository.repositories import UserRepository
from src.services.services import UserService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["src.router.endpoints"])

    config = providers.Configuration(yaml_files=["src/config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
