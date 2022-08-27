"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from src.containers.containers import Container
from src.services.services import UserService

router = APIRouter()


@router.get("/users")
@inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()
