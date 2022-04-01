from flask import render_template, request, jsonify
from app import app
from app.utils.getMsg import *
import json


# 真正调用词云库生成图片
# def get_list():
#     list = getDataList()
#     return jsonify(list)


# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# 生成词云图片接口，以base64格式返回
@app.route('/pcap/analysis', methods=["POST"])
def cloud():
    text = request.json.get("word")
    res = getDataList()
    return res
