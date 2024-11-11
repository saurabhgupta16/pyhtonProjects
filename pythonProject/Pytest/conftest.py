import pytest


@pytest.fixture(scope='class')
def setup():
    print("I am setiing up  the data for your test")
    yield
    print("I am Cleaner and Cleaned up your mess")


@pytest.fixture()
def dataload():
    print(" I am data fairy")
    testdata = ["saurabh","gupta","advisor360.com"]
    return testdata


@pytest.fixture(params=[("Saurabh","Chorme","password"),("Pearl","IE","gupta"),("Kate","Firefox","Godbless")])
def moredata(request):
    return request.param
