import abc

from .scenario import BaseScenario
from .scenario import InternalUserIndexScenario, ExternalUserIndexScenario


class BaseQueryFactory(abc.ABC):

    @abc.abstractmethod
    def create_scenario(self, context) -> BaseScenario:
        pass


class QueryIndexScenarioFactory(BaseQueryFactory):

    def create_scenario(self, context) -> BaseScenario:
        if 'group' in context:
            return InternalUserIndexScenario()
        else:
            return ExternalUserIndexScenario()
