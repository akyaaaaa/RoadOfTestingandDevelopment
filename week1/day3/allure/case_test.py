import pytest


class Testdata:
    def testcase1(self):
        assert 1 == 1

    def testcase2(self):
        assert 1 == 2

    def testcase3(self):

        assert 1 == 3

    def testcase4(self):

        assert 2 == 2

    def testcase5(self):

        assert 1+1 == 2

    def testcase6(self):

        assert 1 == 5
if __name__ == '__main__':
    pytest.main()