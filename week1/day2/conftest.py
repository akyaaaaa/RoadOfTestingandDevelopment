import pytest

def pytest_collection_modifyitems(items):
    """
    修改用例名称中文乱码
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')
    """
    消除mark未识别名称出现的警告
    """
def pytest_configure(config):
    # 把新的加到数组里就行了
    marker_list = ['login']
    for markers in marker_list:
        config.addinivalue_line(
            'markers',markers
        )
'''
定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()，fixture命名不要以test开头，跟用例区分开。
    fixture是有返回值得，没有返回值默认为None。yeild也是返回一个值。用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。
'''
@pytest.fixture(params=[{'lt'}])
def getName(request):
    name = 'lk'
    name1 = request.param

    print('返回name成功')
    return name,name1

@pytest.fixture()
def login():
    print('运行登录方法')

@pytest.fixture()
def login2():
    print('运行登录方法2')

test_data = ['edge','gogle']
@pytest.fixture(scope='function',params=test_data)
# indirect=True 是为了把传过来的open参数当作函数来执行
# @pytest.mark.parametrize('open',testdata,indirect=True)
def open(request):
    # print('打开浏览器')
    # yield
    par = request.param
    result = 'success'
    print('执行teardown')
    print('关闭浏览器')
    return par, result

