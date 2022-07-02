import json

from flask import Flask, url_for, render_template, redirect, session
from auth.routes import blueprint_auth
from report.routes import blueprint_report
from access import login_required


app = Flask(__name__)
app.secret_key = 'SuperKey'

app.register_blueprint(blueprint_auth)
app.register_blueprint(blueprint_report)

app.config['db_config'] = json.load(open('configs/db.json'))
app.config['access_config'] = json.load(open('configs/access.json'))


@app.route('/')
@login_required
def menu_choice():
    if session.get('user_group', None):
        return render_template('internal_user_menu.html')
    return render_template('external_user_menu.html')


@app.route('/exit')
@login_required
def exit_func():
    session.clear()
    return "До свиданья"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
