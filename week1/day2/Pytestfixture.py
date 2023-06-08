import sys

import pytest
# 声明已经放入conftest.py文件 ，运行时会自动先在本文件找fixture参数，然后到到同级文件下找名为conftest的文件
'''
1.在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
2.可以叠加多个 @pytest.mark.usefixtures() ，先执行的放底层，后执行的放上层
3.可以传多个fixture参数，先执行的放前面，后执行的放后面
4,usefixtures与传fixture区别
如果fixture有返回值，那么usefixture就无法获取到返回值，这个是装饰器usefixture与用例直接传fixture参数的区别。
当fixture需要用到return出来的参数时，只能讲参数名称直接当参数传入，不需要用到return出来的参数时，两种方式都可以。

'''
'''@pytest.mark.usefixtures("login2")
class Testdemo:
    def test_Func1(self):
        print('这个需要登录')

    def test_Func2(self):
        print('这个不需要登录')

    def test_Func3(self):
        print('这个需要登录')'''
'''
-----------------------------
@pytest.fixture(scope="session")
def open():
    print("===打开浏览器===")
@pytest.fixture
# @pytest.mark.usefixtures("open") 不可取！！！不生效！！！

def login(open):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{open}")

def test_first(login):
    print('前置条件里面还有前置条件')
------------------------------
    '''

def test_Func1(login):
    print('这个需要登录')

def test_Func2():
    print('这个不需要登录')

def test_Func3(login2):
    print('这个需要登录')

# @pytest.mark.skip(reason='不在windows上执行') 自主跳过
# @pytest.mark.xfail 不跳过，且知道此用例大概是有问题的 提前给其标注一下

@pytest.mark.xfail
def test_name(getName):
    me = getName[0]
    jie = getName[1]
    print(jie)
    assert me=='lk'



if __name__ == '__main__':
    pytest.main()