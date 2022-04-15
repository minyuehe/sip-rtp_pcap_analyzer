from flask import render_template, request, Response, jsonify
from app import app
from app.utils.getMsg import *
from app.utils.uploadFile import *
import json
import os

# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# pcap文件解析接口，以字典形式返回
@app.route('/pcap/analysis', methods=["GET"])
def analysis():
    try: 
        res = getDataList()
    except Exception as err:
        print('err', str(err))
        return str(err), 500
    else:
    # 解析完成删除文件
        os.remove(res[1])
        return res[0], 200

# pcap上传接收接口
@app.route('/pcap/upload', methods=["POST"])
def upload():
    requ_data = {
        'file': request.files.get('file')
    }
    resp_data = resp_file_upload(requ_data)

    return jsonify(resp_data)

# test
@app.route('/print', methods=["POST"])
def printI():
    data = request.data.decode('utf-8')
    value = json.loads(data)['data']
    return value
