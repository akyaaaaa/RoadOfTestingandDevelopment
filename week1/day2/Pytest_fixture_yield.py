import pytest
# 声明已经放入conftest.py文件 ，运行时会自动先在本文件找fixture参数，然后到到同级文件下找名为conftest的文件

def test_Func1(open):
    print('这个需要登录')

def test_Func2(open):
    print('这个需要登录，还携带了参数' % open)

def test_Func3(open):
    print('这个需要登录')

if __name__ == '__main__':
    pytest.main()