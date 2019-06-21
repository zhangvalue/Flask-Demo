# -*- coding:utf-8 -*-

"""
本节讲解如何使用 Jinjia2 模板
"""

from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


# 知识点: Jinjia2 模板的使用
@app.route('/')
def index():
    title = 'Flask Templates'
    return render_template('test1.html', title=title)


@app.route('/test2/')
def index2():
    title = 'Flask Templates'
    users = ['Tom', 'Jerry&Lily', 'Mike']
    book = {
        'title': 'Python',
        'author': 'Tome',
        'price': 28.50,
        'pubdate': datetime.now()
    }
    return render_template('test2.html', title=title, users=users, book=book)


if __name__ == '__main__':
    app.run(debug=True)
