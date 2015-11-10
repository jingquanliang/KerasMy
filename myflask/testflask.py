# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>My Home Page</h1>
        <ul>
            <li><a href="/music">Music</a></li>
            <li><a href="/movie">Movie</a></li>
            <li><a href="/book">Book</a></li>
        </ul>
    '''

@app.route('/auth',methods=['GET','POST'])
def v_auth():
    if request.method == 'GET':
        return '<h1>在这里做验证工作get</h1>'# 返回用户列表
    if request.method == 'POST':
        return '<h1>在这里做验证工作post</h1>'#创建新用户

@app.route('/music',methods=['GET','POST'])
def music():
    return '<h1>My Favorite Music get</h1>'

@app.route('/movie')
def movie():
    return '<h1>My Favorite Movie GET</h1>'
    
@app.route('/book')
def book():
    return '<h1>My Favorite Book</h1>'

app.run(host='0.0.0.0',port=80)
