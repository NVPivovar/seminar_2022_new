import abc

from flask import render_template


class BaseScenario(abc.ABC):

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass


class InternalUserIndexScenario(BaseScenario):

    def execute(self, *args, **kwargs):
        return render_template('internal/query-index.html')


class ExternalUserIndexScenario(BaseScenario):

    def execute(self, *args, **kwargs):
        return render_template('external/query-index.html')
