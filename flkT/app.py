#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: app.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/2/26 9:08

from flask import Flask, render_template

app = Flask(__name__) # 实例化 flask , __name__ 会作为 app 核心的一个标识，这个可以为任意的字符串

@app.route('/') # 使用路由，给 hello 函数定义一个路由，然后游览器通过http 请求得到相对应的数据
def index(): # hello 是视图函数，也是 mvc 中的 controller
    return render_template('index.html')

app.run()