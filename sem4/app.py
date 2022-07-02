import json

from flask import Flask, url_for, render_template, redirect, session
from blueprint_auth.routes import blueprint_auth
from blueprint_report.routes import blueprint_report


app = Flask(__name__)
app.secret_key = 'SuperKey'

app.register_blueprint(blueprint_auth)
app.register_blueprint(blueprint_report)

app.config['db_config'] = json.load(open('configs/db.json'))
app.config['access_config'] = json.load(open('configs/access.json'))


@app.route('/')
def start_point():
    return redirect(url_for('blueprint_auth.start_auth'))


@app.route('/menu_choice')
def menu_choice():
    if session.get('user_group', None):
        return render_template('external_user_menu.html')
    return render_template('internal_user_menu.html')


@app.route('/exit')
def exit_func():
    session.clear()
    return "До свиданья"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
