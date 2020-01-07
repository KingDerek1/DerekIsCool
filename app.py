from flask import Flask, render_template, request, redirect, url_for, session
import urllib.request as urlrequest
import json
import sqlite3, os
from utl.dbfunc import setup, createUser

app = Flask(__name__)

app.secret_key = os.urandom(32)

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

setup(c)

@app.route("/")
def root():
    if "userID" in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route("/login")
def login():
    if "userID" in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route("/signup")
def signup():
    if "userID" in session:
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route("/register", methods=["POST"])
def register():
    error = '';
    if "userID" in session:
        return redirect(url_for('home'))
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    displayname = request.form['displayname']
    email = request.form['email'] + "@stuy.edu"
    c.execute("SELECT username FROM users WHERE username = %s" % username);
    a = c.fetchone()
    if a != None:
        error = 'Username Already Taken'
        return render_template('signup.html', error=error);
    if password != password2:
        error = 'Passwords Don\'t Match'
        return render_template('signup.html', error=error);
    dbfunc.createUser(c, username, password, displayname, email)
    db.commit()
    return redirect(url_for('login'))

@app.route("/auth", methods=['POST'])
def auth():
    if "userID" in session:
        return redirect(url_for('home'))
    username = request.form['username']
    password = request.form['password']
    c.execute("SELECT userID, password FROM users WHERE username = %s" % username)
    a = c.fetchone()
    if a == None:
        error = 'Username Not Found'
        return render_template('login.html', error=error)
    if password != a[1]:
        error = 'Password Incorrect'
        return render_template('login.html', error=error)
    session['userID'] = a[0]
    session['username'] = username
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return "Hello World"

if __name__ == "__main__":
    app.debug = True
    app.run()
