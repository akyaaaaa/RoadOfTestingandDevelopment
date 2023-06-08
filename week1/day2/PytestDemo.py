import pytest


def func(x):
    return x + 1


def test_Func():
    print('执行方法1')
    assert func(3) == 4


class Testdemo:
    def test_Func1(self):
        print('执行方法2')
        # assert func(3) == 6
        pytest.assume(func(3) == 4)
        # assert func(3) == 4
        pytest.assume(func(3) == 4)
        print('断言失败后执行方法')

    def test_Func2(self):
        print('执行方法3')
        assert func(4) == 5
if __name__ == '__main__':
    pytest.main('-v -s')