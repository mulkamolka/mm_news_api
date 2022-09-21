"""Containers module."""
import os

from dependency_injector import containers, providers
from dotenv import load_dotenv

from src.repository.repository import UserRepository
from src.database.orm import Database
from src.services.services import UserService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["src.router.endpoints"])

    db = providers.Singleton(Database, db_url= os.environ.get('DATABASE_URL'))

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository
    )
