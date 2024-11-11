#Any file name need to start with test_ or end with _test
#Function name start with test_
# all test should be wrapped in method
# -k for the Speical Method name and run al the test case which matches it
# -s print logs
# -v More deails
# you can mark a test case and you can run only those by tag
# you can mark a test case s Skip and
#Fixtures are used to write  and  tear down
# you can Write Fixtures in Conftest file and can we called from any method.
#py.test --html=report.html -v -s

import pytest



#@pytest.mark.skip
@pytest.mark.smoke
def test_firsttest(setup):
    print("you are making good progress Saurabh")

@pytest.mark.xfail
@pytest.mark.regression
def test_secondtest():
    print("this is your second test ")

