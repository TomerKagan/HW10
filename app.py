from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session
from pages.Insert_user.Insert_user import Insert_user
from pages.Delete_user.Delete_user import Delete_user
from pages.Update_user.Update_user import Update_user
from pages.assignment10.assignment10 import assignment10

app = Flask(__name__)

app.secret_key = '5198'

# Insert_user
app.register_blueprint(Insert_user)

# Delete_user
app.register_blueprint(Delete_user)

# Update_user
app.register_blueprint(Update_user)

# Assignment10
app.register_blueprint(assignment10)

# This is only for assignment 9 from now on we use db only
users = {'user1': {'name': 'Tomer', 'email': 'tomer66kagan@gmail.com'},
         'user2': {'name': 'Noam', 'email': 'noam98@gmail.com'},
         'user3': {'name': 'Nevo Yehonatan', 'email': 'nevo@gmail.com'},
         'user4': {'name': 'Roy', 'email': 'roy@gmail.com'},
         'user5': {'name': 'Sagi', 'email': 'sagi@gmail.com'}}

@app.route('/')
def main_page():  # put application's code here
    return render_template('index.html')


@app.route('/assignment8')
def assignment():
    return render_template('assignment8.html', hobbies=('playing FIFA', 'reading about space', 'playing basketball'), fav_hobby='spending time with my girlfriend')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if request.args and request.method == 'GET' and request.args['user_name']:
        if request.args['user_name'] != '' and request.args['user_name'] in users:
            user = users.get(request.args['user_name'])
            return render_template('assignment9.html', user=user)
        return render_template('assignment9.html', searched=True)
    elif request.method == 'POST':
        if 'log_out' in request.form:
            session['username'] = ''
        if 'username' in request.form and 'password' in request.form and 'name' in request.form and 'email' in request.form:
            username = request.form['username']
            session['username'] = username
            return render_template('assignment9.html', username=username)
    return render_template('assignment9.html', dic_users=users)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return redirect(url_for('assignment9'))


@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            session['username'] = username
    return redirect(url_for('main_page'))






if __name__ == '__main__':
    app.run()
