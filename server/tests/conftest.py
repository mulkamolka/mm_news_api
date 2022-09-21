import os

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from src.config import Settings, get_settings
from src.main import create_app


def get_settings_test():
    return Settings(
        environment="test", testing=True, database_url=os.environ.get("DATABASE_TEST")
    )


@pytest.fixture(scope="module")
def test_app():

    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_test
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down


@pytest.fixture(scope="module")
def test_app_with_db():

    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_test
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST"),
        modules={"modles": ["src.models.orm"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down
