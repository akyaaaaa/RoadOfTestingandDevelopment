"""
注释
"""
# str = input()
# for s in str:
#
#     if (s == 'e'):
#         print('打印退出')
#         break
#     if (s == 'o'):
#         print('打印跳过')
#         continue
#     print(s)
flag = 'good good study'
a='123'
# print('lk'.join(flag.split('oo')))
demo = ['1',2,2,True]
demo1 = [23,444]
demo.append(2)
demo.insert(0,'frist')
demo.insert(-1,'end')
demo.extend(demo1)
# print(demo.count(2))
# demo.reverse()
num = (1,23,4,555,7)

# print(num.index(555))
dict = {'name':'lk','sex':'nan','age':'20'}
for i in dict.items():
    print(i)
def add(a,b):
    return a+b+num()
def num():
    return input()
print(add('3','4'))

