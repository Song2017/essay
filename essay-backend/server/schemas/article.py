from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: Optional[str]
    desc: Optional[str]
    content: str
    img_url: Optional[str]


class ArticleCreate(ArticleBase):
    ...


class ArticlePut(ArticleBase):
    essay_article_id: Optional[int]


class ArticleOrm(ArticleBase):
    """
    """
    essay_article_id: Optional[int]
    create_time: Optional[datetime]
    modify_time: Optional[datetime]
    create_by: Optional[str]
    modify_by: Optional[str]

    class Config:
        orm_mode = True
