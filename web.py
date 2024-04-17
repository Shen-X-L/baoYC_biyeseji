
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename  # 导入secure_filename函数

# 创建一个Flask应用实例  
app = Flask(__name__)
#定义一个字符串变量，用于指定上传文件的保存目录
UPLOAD_FOLDER = 'uploads'
#将上传文件夹的路径添加到Flask应用的配置中。
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 定义一个路由和处理函数 回归分析URL地址在ip:端口/huigui/或/regression/
@app.route('/huigui/')
@app.route('/regression/')
def regression():
    return render_template('regression.html')

@app.route('/fenlei/')
@app.route('/classification/')
def classification():
    return render_template('classification.html')

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件部分
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # 如果用户没有选择文件，浏览器也会提交一个空文件部分，没有文件名
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = secure_filename(file.filename)  # 使用secure_filename确保文件名安全
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
    return render_template('upload.html')

    # 如果运行这个脚本，则启动开发服务器
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)