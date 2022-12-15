from typing import Any, List, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api import deps
from db.crud.base import CRUDBase
from models.essay_article import EssayArticle
from schemas.article import ArticleCreate, ArticlePut, ArticleOrm

router = APIRouter()


@router.post("/")
def create_info(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: ArticleCreate,
        _=Depends(deps.get_current_active_user),
) -> Any:
    auth = CRUDBase(EssayArticle)
    return auth.create(db, obj_in=obj_in)


@router.put("/")
def put_auth(
        obj_in: ArticlePut,
        db: Session = Depends(deps.get_db),
        _=Depends(deps.get_current_active_user),
) -> Any:
    """
    Test access token
    """
    auth = CRUDBase(EssayArticle)
    res = auth.query_update(db, condition_in={
        "essay_article_id": obj_in.essay_article_id}, obj_in=obj_in)
    if not res:
        raise HTTPException(status_code=400, detail="No record update")
    return obj_in


@router.get("/", response_model=List[ArticleOrm])
def get_article(
        *,
        article_id: Union[int, None] = None,
        name: Union[str, None] = None,
        page_no: int = 1,
        page_size: int = 10,
        db: Session = Depends(deps.get_db),
        # _=Depends(deps.get_current_active_user),
) -> Any:
    operation = CRUDBase(EssayArticle)
    condition_in = {"name": name, "essay_article_id": article_id}
    info = operation.get_multi(db, page_no=page_no, page_size=page_size,
                               condition_in=condition_in, order_by="essay_article_id")
    return info
