from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def main_page():  # put application's code here
    return render_template('index.html',  personalDetails={'first_name': 'Tomer', 'last_name': "Kagan"})


@app.route('/assignment8')
def assignment():
    return render_template('assignment8.html', personalDetails={'first_name': 'tomer', 'last_name': "kagan"}, hobbies=('playing FIFA', 'reading about space', 'playing basketball'), fav_hobby='spending time with my girlfriend')


if __name__ == '__main__':
    app.run()
