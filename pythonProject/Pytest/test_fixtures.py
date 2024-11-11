import pytest



@pytest.mark.usefixtures("setup")
class TestEample:

    def test_psrlookup1(self):
        print("click on the user1 name ")


    def test_psrlookup2(self):
        print("click on the user2 name ")


    def test_psrlookup3(self):
        print("click on the user3 name ")


    def test_psrlookup4(self):
        print("click on the user4 name ")
