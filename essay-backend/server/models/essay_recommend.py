from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP

from db.postgres.base_models import Base, ReprMixin


class EssayRecommend(Base, ReprMixin):
    __tablename__ = 'essay_recommend'

    essay_recommend_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    img_url = Column(String)
    create_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    create_by = Column(String(100))
    modify_by = Column(String(100))
