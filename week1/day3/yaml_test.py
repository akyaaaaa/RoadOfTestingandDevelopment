import pytest
import yaml

# with open('./info.yaml', 'r', encoding='utf-8') as f:
#     info = yaml.safe_load(f)
# print(info)

# @pytest.mark.parametrize('inf', info)
# def testdata(inf):
#     print(f'inf:{inf}')
#     if 'test' in inf:
#         print('这是测试环境')
#     else:
#         print('这不是测试环境')

@pytest.mark.parametrize('inf', yaml.safe_load_all(open('./info.yaml', 'r', encoding='utf-8')))
def testdata(inf):
    # inf:{'data1': [{'name': 'lk'}, {'age': 22}]}
    print(inf["data1"][0]['name'])

    # if 'test' in inf:
    #     print('这是测试环境')
    # else:
    #     print('这不是测试环境')

if __name__ == '__main__':
    pytest.main()
