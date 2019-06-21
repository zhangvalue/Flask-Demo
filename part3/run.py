# -*- coding:utf-8 -*-

"""
本节讲解,不使用SQLAlchemy,直接连接数据库操作
"""

import pymysql as MySQLdb
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


# 查看列表
@app.route('/business/')
def business_list():
    conn = MySQL()
    business = conn.execute('select `id`, `name`, `level_type`, `status` from business where status=1 and belong_type=1;')
    conn.close()
    print('business===', business)
    return render_template('business-list.html', business=business)


# 增删改查都是直接通过 sql 语句操作,此处不扩展讲解


# 数据库连接
class MySQL:

    def __init__(self):
        config = {
            'user': 'root',
            'password': '123456',
            'host': '127.0.0.1',
            'db': 'monitor_tool',
            'port': 3306,
            'raise_on_warnings': True
        }
        try:
            self.conn = MySQLdb.connect(host=config['host'], port=config['port'], user=config['user'],
                                        passwd=config['password'], db=config['db'], charset="utf8", use_unicode=True)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(('Connect fails!{}'.format(e)))
            raise e

    def execute(self, sql):  # Remember COMMIT after your non-query execution!
        """
        @summary: Execute SQL statement
        @param sql:
        @return:
        """

        self.cursor.execute(sql)
        result = []
        for i in self.cursor:
            result.append(i)
        self.conn.commit()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # sql = 'select * from business;'
    # print(MySQL().execute(sql))
    app.run(debug=True)
