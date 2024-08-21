from flask import *
import json,time
from os import path,listdir

app = Flask(__name__)

def getbook(f):
    rec = listdir(path.join('book',f))
    for i in range(len(rec)):
        for j in range(len(rec[i])-1,-1,-1):
            if rec[i][j]=='.':
                break
        rec[i] = rec[i][:j]
    return rec

def tfile(name,tmp):
    if tmp=='r':
        return open(str(name),'r',encoding='UTF-8').read()
    open(str(name),'w',encoding='UTF-8').write(str(rec))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booklist')
def booklist():
    return json.dumps(getbook('txt'))

@app.route('/upload',methods=['POST'])
def upload():
    form = request.form
    if form['name'] not in getbook(form['type']):
        tfile(path.join('book',form['type'],name),form['content'])
        return 'success'
    else:
        pass
    return ''

app.run('0.0.0.0',port=5000)
