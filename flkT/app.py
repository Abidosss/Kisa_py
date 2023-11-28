# Refer: https://hackmd.io/@shaoeChen/rkpy9CGZz?type=view

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)



def adder(num):
    return 10+int(num)


def encrypt():
    return


def decrypt():
    return

# Test Text
name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)


@app.route('/ad',methods=['GET','POST'])
def play():
    if request.method == 'POST':
        return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('playground.html')


@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('hello', username=request.form.get('username')))

    return render_template('login.html')


@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)


@app.route('/cpaa', methods=['GET', 'POST'])
def cp():
    if request.method == 'POST':
        return 'Hello ' + request.values['username']
    return render_template('cipher.html')


app.debug = True
app.run()
