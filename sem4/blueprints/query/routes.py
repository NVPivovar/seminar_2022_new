from flask import Blueprint, session
from .factory import QueryIndexScenarioFactory

query_app = Blueprint('query', __name__, template_folder='templates')


@query_app.route('/')
def query_index():
	scenario = QueryIndexScenarioFactory().create_scenario(context=session)
	return scenario.execute()
