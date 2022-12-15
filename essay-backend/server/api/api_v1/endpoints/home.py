from typing import Any, List, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api import deps
from db.crud.base import CRUDBase
from models.essay_article import EssayArticle

router = APIRouter()


@router.get("/home")
def get_home(
        *,
        db: Session = Depends(deps.get_db),
        # _=Depends(deps.get_current_active_user),
) -> Any:
    home_page_articles = {
        "topicList": [{
            "id": 1,
            "title": "Topic",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
        }],
        "articleList": [],
        "recommendList": [{
            "id": 1,
            "imgUrl": "https://img1.baidu.com/it/u=105002249,3897918256&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=281"
        }, {
            "id": 2,
            "imgUrl": "https://img0.baidu.com/it/u=2028084904,3939052004&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500"
        }]
    }
    operation = CRUDBase(EssayArticle)
    info = operation.get_multi(db, page_no=1, page_size=5,
                               condition_in={}, order_by="essay_article_id")
    home_page_articles["articleList"] = [{
        "id": item.essay_article_id,
        "desc": item.desc,
        "title": item.title,
        "img_url": item.img_url,
    } for item in info]
    return {"success": True, "data": home_page_articles}


@router.get("/home-list")
def get_home_list(
        *,
        page_no: int = 1,
        db: Session = Depends(deps.get_db),
        _=Depends(deps.get_current_active_user),
) -> Any:
    operation = CRUDBase(EssayArticle)
    info = operation.get_multi(db, page_no=page_no, page_size=1,
                               condition_in={}, order_by="essay_article_id")
    return {"success": True, "data": info}


@router.get("/header-list")
def get_header(
        *,
        page_no: int = 1,
        db: Session = Depends(deps.get_db),
        _=Depends(deps.get_current_active_user),
) -> Any:
    header_list_articles = [
        "高考", "区块链", "三生三世", "崔永元", "vue", "小程序", "茶点微小说",
        "萨沙讲史堂", "夜幕下的地安门", "擦亮你的眼", "理财", "毕业", "手帐",
        "简书交友", "spring", "古风", "故事", "暖寄归人", "旅行", "连载", "教育",
        "简书",
        "生活", "投稿", "历史", "PHP", "考研", "docker", "EOS", "微信小程序",
        "PPT", "职场", "大数据", "创业", "书评", "东凤", "饱醉豚", "雨落荒原",
        "程序员", "爬虫", "时间管理", "kotlin", "数据分析", "阴阳合同", "设计",
        "红楼梦", "父亲节", "女人和衣服", "swift", "高考作文"]
    return {"success": True, "data": header_list_articles}
