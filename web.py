# 导入Flask类  
from flask import Flask, render_template

# 创建一个Flask应用实例  
app = Flask(__name__)


# 定义一个路由和处理函数
@app.route('/show')
def hello_world():
    return render_template('index.html')


# 如果运行这个脚本，则启动开发服务器
if __name__ == '__main__':
    app.run()