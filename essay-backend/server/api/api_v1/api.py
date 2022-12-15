from fastapi import APIRouter

from api.api_v1.endpoints import login, article, home

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(article.router, prefix="/article", tags=["article info"])
api_router.include_router(home.router, tags=["home info"])
