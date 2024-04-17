
from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
# 数据库连接配置
DATABASE_URL = 'mysql+pymysql://username:password@localhost:3306/mydatabase'
engine = create_engine(DATABASE_URL)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/upload', methods=['POST'])
def upload_excel():
    # 获取上传的Excel文件
    file = request.files['excel_file']
    # 使用pandas读取Excel文件
    df = pd.read_excel(file)
    # 将DataFrame内容写入数据库
    df.to_sql('my_table', engine, if_exists='append', index=False)
    return 'Excel file uploaded and data imported into the database successfully!'

if __name__ == '__main__':
    app.run(debug=True)