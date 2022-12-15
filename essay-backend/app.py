from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import uuid, json

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

home_page_articles = {
        "topicList": [{
            "id": 1,
            "title": "Topic",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
        }],
        "articleList": [{
            "id": 1,
            "title": "胡歌12年后首谈车祸",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
        }, {
            "id": 2,
            "title": "胡歌12年后首谈车祸：既然活下来了，就不能白白活着",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
        }, {
            "id": 3,
            "title": "胡歌12年后首谈车祸：既然活下来了，就不能白白活着",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
        }, {
            "id": 4,
            "title": "胡歌12年后首谈车祸：既然活下来了，就不能白白活着",
            "desc": "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
        }],
        "recommendList": [{
            "id": 1,
            "imgUrl": "https://img1.baidu.com/it/u=105002249,3897918256&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=281"
        }, {
            "id": 2,
            "imgUrl": "https://img0.baidu.com/it/u=2028084904,3939052004&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500"
        }]
    }
home_articles = [{
    "id":
        5,
    "title":
        "胡歌12年后首谈车祸1",
    "desc":
        "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
    "imgUrl":
        "https://img2.baidu.com/it/u=1361506290,4036378790&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500"
}, {
    "id":
        6,
    "title":
        "胡歌12年后首谈车祸：既然活下来了，就不能白白活着2",
    "desc":
        "文/麦大人 01 胡歌又刷屏了。 近日他上了《朗读者》，而这一期的主题是“生命”，他用磁性的嗓音，朗读了一段《哈姆雷特》中的经典独白，相当震撼：...",
    "imgUrl":
        "https://img0.baidu.com/it/u=2243264347,2203972402&fm=253&fmt=auto&app=120&f=JPEG?w=1280&h=800"
}]

# sanity check route
@app.route('/api/home', methods=['GET'])
def home():
    resp = {"success": True, "data": home_page_articles}
    rst = make_response(json.dumps(resp))
    return rst

@app.route('/api/article', methods=['POST'])
def article():
    len_topic = len(home_page_articles["articleList"]) + 1
    body = request.get_json()
    print(body)
    home_page_articles["articleList"].append({
            "id": len_topic,
            "title": body.get("title") or "title",
            "desc": body.get("content") or "content",
            "imgUrl": "https://img2.baidu.com/it/u=2124229159,1459379647&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500"
    })
    resp = {"success": True, "data": home_page_articles}
    rst = make_response(json.dumps(resp))
    return rst

@app.route('/api/homeList', methods=['GET'])
def home_list():
    resp = {"success": True, "data": []}
    if request.args.get('page'):
        resp['data'] = [home_articles[int(request.args.get('page')) % 2]]
        rst = make_response(json.dumps(resp))
        return rst


@app.route('/api/headerList', methods=['GET'])
def header_list():
    header_list_articles = [
        "高考", "区块链", "三生三世", "崔永元", "vue", "小程序", "茶点微小说",
        "萨沙讲史堂", "夜幕下的地安门", "擦亮你的眼", "理财", "毕业", "手帐",
        "简书交友", "spring", "古风", "故事", "暖寄归人", "旅行", "连载", "教育",
        "简书",
        "生活", "投稿", "历史", "PHP", "考研", "docker", "EOS", "微信小程序",
        "PPT", "职场", "大数据", "创业", "书评", "东凤", "饱醉豚", "雨落荒原",
        "程序员", "爬虫", "时间管理", "kotlin", "数据分析", "阴阳合同", "设计",
        "红楼梦", "父亲节", "女人和衣服", "swift", "高考作文"]

    resp = {"success": True, "data": header_list_articles}
    rst = make_response(json.dumps(resp))
    return rst


@app.route('/api/login', methods=['GET'])
def login():
    rst = make_response(json.dumps({
        "success": True,
        "data": True
    }))
    return rst


@app.route('/api/detail', methods=['GET'])
def detail():
    if request.args.get('id'):
        print(request.args.get('id'))
    resp = {
        "success": True,
        "data": {
            "title": "衡水中学，被外地人占领的高考工厂",
            "content": "衡水中学，被外地人占领的高考工厂 content"
        }}
    rst = make_response(json.dumps(resp))
    return rst


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)
