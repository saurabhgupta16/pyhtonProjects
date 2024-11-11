import pytest
from Pytest.Logbase import logFunction


@pytest.mark.usefixtures("dataload")
class TestlogExample(logFunction):

    def test_datalog(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])
        log.info(dataload[2])


