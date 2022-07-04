import os

from flask import Blueprint, render_template, request, current_app

from database.operations import select
from database.sql_provider import SQLProvider


blueprint_market = Blueprint(
	'blueprint_market',
	__name__,
	template_folder='templates',
	static_folder='static'
)
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_market.route('/', methods=['GET', 'POST'])
def market_index():
	if request.method == 'GET':
		category = request.args.get('category', None)
		if category:
			min_price = request.args.get('price-range', 0)
			sql = provider.get('items_from_category.sql', category=category, min_price=min_price)
		else:
			sql = provider.get('all_items.sql')
		items = select(current_app.config['db_config'], sql)
		return render_template('market/index.html', items=items)
	else:
		return 'Страница не найдена'
