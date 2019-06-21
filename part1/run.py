# -*- coding:utf-8 -*-

"""
本节讲解Flask 快速实例 及 Flask 核心对象之request
"""

from flask import Flask, render_template, request, redirect, jsonify, url_for


# 通过Flask 类构造程序对象
app = Flask(__name__)  # 说明run.py 以这里为起点
# app.debug = True     # 调试方法也可以写在这里，True 是启用调试，False 不启用调试


@app.route('/')        # 使用装饰器匹配一个url
@app.route('/hello')   # 可以有多个装饰器
def index():           # 用于响应的函数，叫视图函数
    return 'hello'


@app.route('/re-json')
def re_json():
    res = {'key': 'hello'}
    return jsonify(res)


# @app.route('/html') 如果没有斜杠，则在访问时有/时就访问不了
# 如果有/ 在访问/html 时会自动加上/，推荐用后面 有/ 的方法 @app.route('/html/')
@app.route('/html/')
def html():
    html = """
    <html>
        <head>
            <title>Flask demo </title>
        </head>
        <body>
            <h1>baidu.com</h1>
            <img src="https://www.baidu.com/img/baidu_jgylogo3.gif" />
        </body>
    </html>
    """
    return html


# 请求响应模板HTML, 使用render_template
@app.route('/template/')
def html_template():
    return render_template('html_template.html')   # render_template 呈现模板


# 往html 模板中加变量数据
@app.route('/products/')
def product_list():
    items = [
        (1, 'iPhone4s', 2900.00, None, '2016-05-04'),
        (2, 'iPhone5s', 3900.00, None, '2016-05-05'),
        (3, 'iPhone6s', 4900.00, None, '2016-05-06'),
        (4, 'iPhone7s', 5900.00, None, '2016-05-07')
    ]
    title = '一季度产品库存'
    return render_template('product-list.html', pro_title=title, data=items)


# 对比 product-list.html 获取字段的方法,优点
@app.route('/products2/')
def product_list2():
    title = "http:/baidu.com"
    employee = {
        'name': 'Tom',
        'age': 22,
        'job': 'dev'
    }
    return render_template('product-list2.html', title=title, data=employee)


# 视图函数参数，地址栏参数
@app.route('/hello/<name>/')        # @app.route('/hello/<int:name>') 限制类型是int型
def hello(name):
    return '您好:{}'.format(name)


# 知识点：get请求，获取浏览器地址栏输入的值 request.args.get['key']
# 测试地址：http://127.0.0.1:5000/request/querystring/?name=tom&id=5
@app.route('/request/querystring/')
def request_querystring():
    name = request.args.get('name', '未找到')
    id = request.args.get('id', 0)
    return "名称：{}， 编号：{}".format(name, id)


# 知识点：url_for、redirect
# redirect 类是转跳功能
# url_for 根据终结点的名称(方法名称)来生成url 地址
@app.route('/redirect/')
def redirect_to():
    # return redirect('/request/querystring/')
    return redirect(url_for('request_querystring'))


# 知识点：获取请求信息request
@app.route('/request/other/')
def request_other():
    data = {}
    data['ip'] = request.remote_addr       # 访问的客户端的IP地址
    data['environ'] = request.environ      # 客户端环境
    data['method'] = request.method        # 访问的方法
    data['path'] = request.path            # 客户端请求路径
    data['full_path'] = request.full_path  # 客户端请求完整路径
    data['url'] = request.url              # 请求url
    data['base_url'] = request.base_url    # 基本url
    data['is_xhr'] = request.is_xhr        # 是否是ajax 请求
    # data['module'] = request.module        # 当前所处的模块
    data['endpoint'] = request.endpoint    # 当前终结点，就是函数的名称
    data['url_rule'] = request.url_rule    # url 规则
    data['view_args'] = request.view_args  # 视图参数

    return render_template('request-other.html', data=data)


# 知识点：获取代理浏览器的信息User_Agent
@app.route('/request/headers/')
def request_header():
    user_agent = request.headers['User_Agent']
    return user_agent


# 知识点：获取浏览器完整的头部信息 request.headers
@app.route('/request/headers2/')
def request_header2():
    headers = dict(request.headers)
    return render_template('request-header.html', headers=headers)


# 知识点：post请求，获取form 提交的参数信息 request.form['key']
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']   # email 匹配的是html 中的 name，不是id
        password = request.form['pwd']
        remember = request.form.get('remember', None)  # 如果写 request.form['remember'] 那么在未勾选记住我的时候后台获取不到值会报Bad Request
        return render_template('form-data.html', email=email, password=password, remember=remember)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)      # run 是方法，不是函数
