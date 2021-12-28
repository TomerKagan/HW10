from flask import Flask, redirect, url_for, render_template
from flask import request

app = Flask(__name__)

users = {'user1': {'name': 'Tomer', 'email': 'tomer66kagan@gmail.com'},
         'user2': {'name': 'Noam', 'email': 'noam98@gmail.com'},
         'user3': {'name': 'Nevo Yehonatan', 'email': 'nevo@gmail.com'},
         'user4': {'name': 'Roy', 'email': 'roy@gmail.com'},
         'user5': {'name': 'Sagi', 'email': 'sagi@gmail.com'}}


@app.route('/')
def main_page():  # put application's code here
    return render_template('index.html',  personalDetails={'first_name': 'Tomer', 'last_name': "Kagan"})


@app.route('/assignment8')
def assignment():
    return render_template('assignment8.html', personalDetails={'first_name': 'tomer', 'last_name': "kagan"}, hobbies=('playing FIFA', 'reading about space', 'playing basketball'), fav_hobby='spending time with my girlfriend')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    personal_details = {'first_name': 'Tomer', 'last_name': "Kagan"}
    if request.args and request.method == 'GET' and request.args['user_name']:
        if request.args['user_name'] != '' and request.args['user_name'] in users:
            user = users.get(request.args['user_name'])
            return render_template('assignment9.html', user=user, personalDetails=personal_details)
        return render_template('assignment9.html', personalDetails=personal_details, searched=True)
    return render_template('assignment9.html', dic_users=users, personalDetails=personal_details)


if __name__ == '__main__':
    app.run()
