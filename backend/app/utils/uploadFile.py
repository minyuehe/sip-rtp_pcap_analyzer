import os

def resp_file_upload(requ_data):
    # 保存文件
    file_content = requ_data['file']
    file_name = requ_data['file'].filename
    file_path = 'app/download/' + file_name
    if os.path.exists(file_path):
        return {'msg': '该文件已存在'}
    else:
        file_content.save(file_path)
        return {'msg': '保存文件成功'}
