# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EssayArticle(Base):
    __tablename__ = 'essay_article'

    essay_article_id = Column(Integer, primary_key=True, server_default=text("nextval('essay_article_essay_article_id_seq'::regclass)"))
    title = Column(String(100))
    desc = Column(String(100))
    content = Column(String)
    img_url = Column(String)
    create_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    create_by = Column(String(100))
    modify_by = Column(String(100))


class EssayRecommend(Base):
    __tablename__ = 'essay_recommend'

    essay_recommend_id = Column(Integer, primary_key=True, server_default=text("nextval('essay_recommend_essay_recommend_id_seq'::regclass)"))
    name = Column(String(100))
    img_url = Column(String)
    create_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    create_by = Column(String(100))
    modify_by = Column(String(100))


class EssayTopic(Base):
    __tablename__ = 'essay_topic'

    essay_topic_id = Column(Integer, primary_key=True, server_default=text("nextval('essay_topic_essay_topic_id_seq'::regclass)"))
    title = Column(String(100))
    img_url = Column(String)
    create_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    modify_time = Column(TIMESTAMP(True, 3), server_default=text("CURRENT_TIMESTAMP"))
    create_by = Column(String(100))
    modify_by = Column(String(100))
