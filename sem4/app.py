import json
from typing import List, Callable

from flask import Flask, render_template

app = Flask(__name__)

app.config['DB_CONFIG'] = json.load(open('configs/db.json'))
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))
app.config['SECRET_KEY'] = 'super secret key'

from blueprints.auth.routes import auth_app
from blueprints.admin.routes import admin_app
from blueprints.query.routes import query_app

app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(admin_app, url_prefix='/admin')
app.register_blueprint(query_app, url_prefix='/query')


@app.route('/')
def index():
    return render_template('index.html')


def add_blueprint_access_handler(app: Flask, blueprint_names: List[str], handler: Callable) -> Flask:
    for view_func_name, view_func in app.view_functions.items():
        view_func_parts = view_func_name.split('.')
        if len(view_func_parts) > 1:
            view_blueprint = view_func_parts[0]
            if view_blueprint in blueprint_names:
                view_func = handler(view_func)
                app.view_functions[view_func_name] = view_func
    return app


if __name__ == '__main__':
    # app = add_blueprint_access_handler(app, ['query', 'admin'], AccessManager.group_required)
    app.run(host='0.0.0.0', port=5001)
