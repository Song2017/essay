from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP

from db.postgres.base_models import Base, ReprMixin


class EssayArticle(Base, ReprMixin):
    __tablename__ = 'essay_article'

    essay_article_id = Column(Integer, primary_key=True)
    title = Column(String(100))
    desc = Column(String(100))
    content = Column(String)
    img_url = Column(String)
    create_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    create_by = Column(String(100))
    modify_by = Column(String(100))
