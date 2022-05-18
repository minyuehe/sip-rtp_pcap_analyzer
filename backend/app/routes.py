from flask import render_template, request, Response, jsonify
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
        try:
            if(len(res[0])<=2):
                raise Exception("亲，该pcap文件无SIP/RTP通信数据")
        except Exception as err:
            return str(err), 500
        else:
            return res[0], 200

# pcap上传接收接口
@app.route('/pcap/upload', methods=["POST"])
def upload():
    print(request.remote_addr)
    requ_data = {
        'file': request.files.get('file')
    }
    resp_data = resp_file_upload(requ_data)

    return jsonify(resp_data)

