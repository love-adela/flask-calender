from flask import Flask 
from flask import render_template, request
import argon2

import db

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form['username']
    cursor = db.conn.cursor()
    cursor.execute('select password_hash, password_salt from account where username=%s;', [username])
    result = cursor.fetchone()
    cursor.close()

    if result is None:
        return 'Fail'

    db_hash = result[0]
    salt = result[1]
    user_hash = argon2.argon2_hash(request.form['password'], salt).hex()

    if db_hash == user_hash:
        return 'Success'
    else:
        return 'Fail'
    return 'testing'
