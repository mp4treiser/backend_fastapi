from typing import Union

from fastapi import APIRouter

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@router.get("/")
def read_root():
    return {"Hello": "World"}