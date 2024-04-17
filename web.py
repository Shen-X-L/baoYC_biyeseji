
import os
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sqlalchemy import create_engine


# 创建一个Flask应用实例  
app = Flask(__name__)
#定义一个字符串变量，用于指定上传文件的保存目录
UPLOAD_FOLDER = 'uploads'
#将上传文件夹的路径添加到Flask应用的配置中。
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)
# 数据库连接配置
DATABASE_URL = 'mysql+pymysql://username:password@localhost:3306/mydatabase'
engine = create_engine(DATABASE_URL)

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
def upload_excel_to_database():
    if request.method == 'POST':
        try:
            # 获取上传的Excel文件
            file = request.files['excel_file']
            # 使用pandas读取Excel文件
            df = pd.read_excel(file)
            # 将DataFrame内容写入数据库
            df.to_sql('my_table', engine, if_exists='append', index=False)
            return 'Excel file uploaded and data imported into the database successfully!'
        except Exception as e:
            # 如果发生异常，返回包含详细错误信息的响应
            return jsonify({'error': str(e)}), 500
    return render_template('upload.html')

    # 如果运行这个脚本，则启动开发服务器
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)