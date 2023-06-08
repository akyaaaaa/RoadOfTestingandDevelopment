import pytest
'''
优先级从高到低
模块级
setup_module teardown_module
函数级
setup_function teardown_function
类级
setup_class teardown_class
方法级
setup_method teardown_method
方法级
setup teardown
————————————————

'''
def setup_module():
    print('setup_module在模块初始换之前执行')
def teardown_module():
    print('teardown_module在模块初始换之后执行')

def func(x):
    return x + 1

def setup_function():
    print('setup_function在函数用例执行之前执行')
def teardown_function():
    print('teardown_function在函数用例执行之后执行')
def test_Func():
    print('执行方法1')
    assert func(3) == 4


class Testdemo:
    '''
    注意值几个要写在class里面
    '''
    def setup_class(self):
        print('setup_class在类用例执行之前执行')
    def teardown_class(self):
        print('teardown_class在类用例执行之后执行')

    def setup(self):
        print('setup执行')
    def teardown(self):
        print('teardown执行')

    def setup_method(self):
        print('setup_method在method用例执行之前执行')
    def teardown_method(self):
        print('teardown_method在method用例执行之后执行')


    # ---------------------------------
    def test_Func1(self):
        print('执行方法2')
        pytest.assume(func(3) == 4)

    def test_Func2(self):
        print('执行方法3')
        assert func(4) == 5
if __name__ == '__main__':
    pytest.main()