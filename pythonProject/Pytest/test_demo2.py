
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_thirdtest():
    msg = "Pearl"
    assert msg == "gupta", "Nope it is not mathcng so i m failing this test"
    print(msg)


@pytest.mark.regression
def test_fourthtest(setup):
    a=4
    b=6
    assert a+2==b, "this is failed , not sure why"
    print(a,b)