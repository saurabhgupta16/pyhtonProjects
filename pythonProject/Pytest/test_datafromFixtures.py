import pytest

@pytest.mark.usefixtures("dataload")
class TestDataDemo:
    def test_data(self,dataload):
        print("I am going to use the data from Fixture")
        print(dataload)