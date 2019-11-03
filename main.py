from flask import Flask 
from flask import render_template, request

import db

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form['username']
    cursor = db.conn.cursor()
    cursor.execute('select password from account where username=%s;', [username])
    result = cursor.fetchone()
    cursor.close()
    print(username, result[0], request.form['password'])
    if result[0] == request.form['password']:
        return 'Success'
    else:
        return 'Fail'
    #TODO:PW는 키 파생 함수를 사용해서 단방향 암호화된 값을 저장하자
    return 'testing'
