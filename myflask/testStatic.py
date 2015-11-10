# -*- coding:utf-8 -*-
def init_static_folder(app):
    import os
    try:
        os.mkdir(os.path.join(app.root_path,'assets'))
        f = open(os.path.join(app.root_path,'assets','1.txt'),'w')
        f.write('this is a static file')
        f.close()
    except:
        pass

from flask import Flask

app = Flask(__name__,static_folder='assets',static_url_path='/mylib')

@app.route('/')
def v_index():
    return '''
        <h1>Home Page</h1>
        <a href="/mylib/1.txt">1.txt</a>
    '''

init_static_folder(app)

app.run(host='0.0.0.0',port=80)



