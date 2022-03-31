from flask import render_template
from flask import request
from app import app


# 真正调用词云库生成图片
def get_list(text):
    print(text)
    return text


# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# 生成词云图片接口，以base64格式返回
@app.route('/pcap/analysis', methods=["POST"])
def cloud():
    text = request.json.get("word")
    res = get_list(text)
    return res
