'''
参数化实战
https://blog.csdn.net/csdnchengxi/article/details/
122578764?ops_request_misc=%257B%2522request%255Fid%2522%253A%25221
68612857816800182146955%2522%252C%2522scm%2522%253A%252220140713.130102334..%
2522%257D&request_id=168612857816800182146955&biz_id=0&utm_medium=di
stribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-3-12
2578764-null-null.142^v88^control_2,239^v2^insert_chatgpt&utm_term=parame
trize&spm=1018.2226.3001.4187
'''
import pytest
# 字典方式
test_data = [
    {
        'usr': 'admin',  # 预期正常登入
        'psw': '123456',
        'expect': '正常登入'
    },
    {
        'usr': 'admin1',  # 账号不存在
        'psw': '123456',
        'expect': '账号不存在'
    },
    {
        'usr': 'admin',  # 密码错误
        'psw': '12345',
        'expect': '密码错误'

    },
    {
        'usr': '',  # 账号或密码为空
        'psw': '',
        'expect': '账号或密码为空'
    },
]
test_user_data = ['Tom', 'Jerry']

# ---------使用parametrize实现参数化----------------------------
# ids为设置用例的名称
'''
parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)

@pytest.mark.parametrize('param', test_data,ids=[data.get('expect') for data in test_data])
def test_login(param):  # 这个param需要和上面的'param'一致
    user = param.get('usr')
    psw = param.get('psw')
    expe = param.get('expect')
    print(f'user:{user} psw:{psw} expe:{expe}')  # 打印

def test_login(param):  # 这个param需要和上面的'param'一致
    user = param.get('usr')
    psw = param.get('psw')
    expe = param.get('expect')
    print(f'user:{user} psw:{psw} expe:{expe}')  # 打印'''
# ----------------------------------------------------------
# ---------使用fixture实现参数化----------------------------
'''
fixture提供了这么一个机制，fixture装饰的函数拥有一个内置的对象request，同时fixture中还有一个params参数是用来传递参数化数据的
'''
'''@pytest.fixture(params=test_data,ids=[data.get('expect') for data in test_data])
def tes_data(request):
    return request.param

def test_login(tes_data):
    user = tes_data.get('usr')
    psw = tes_data.get('psw')
    expe = tes_data.get('expect')
    print(f'user:{user} psw:{psw} expe:{expe}')  # 打印'''
# ---------------------------------------------------------

@pytest.fixture(ids=[data.get('expect') for data in test_data])
def tes_data(request):
    return request.param
# 注意上面的fixture中没有给出params,而是在下面的argvalues=参数中给的，原因是indirect=True
@pytest.mark.parametrize(argnames='tes_data',argvalues=test_data,indirect=True)
def test_data(tes_data):
    a = tes_data
    print(f"测试用例中 login_r 函数 的返回值； {a}")

# ---------------------------------------------------------

# ---------------------------------------------------------
if __name__ == '__main__':  # 定义主函数
    pytest.main()  # 调用pytest
