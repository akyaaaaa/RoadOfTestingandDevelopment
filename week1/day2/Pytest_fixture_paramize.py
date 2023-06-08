import pytest
@pytest.mark.parametrize('testdata,expectation',[(3,3),(4,5)])
def test_eval(testdata,expectation):
    assert testdata == expectation

# a:1,b:2 a:3,b:4
# @pytest.mark.parametrize('a,b',[[1,2],[3,4]])

# a:3,b:3  a:4,b:5
@pytest.mark.parametrize('a,b',[[3,3],[4,5]])
def test_combination(a,b):
    print(f'a:{a},b:{b}')

@pytest.mark.parametrize('a',[1,2])
@pytest.mark.parametrize('b',[3,4,5])

def test_combination(a,b):
    print(f'a:{a},b:{b}')

def test_param(open):
    browser, result = open
    print("在测试用例里面里面获取到当前测试数据：%s" % browser)
    assert result == "success"