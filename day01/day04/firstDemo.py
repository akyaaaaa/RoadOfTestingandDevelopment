"""
lambda
"""


# # 返回字典中键为name的值
# func = lambda dict : dict.get('name')
# print(func({'age':2,'name':1}))
# # 字典排序
# list1 = [{'age':4,'name':1},{'age':2,'name':1},{'age':1,'name':1},{'age':3,'name':1}]
#
# list1.sort(key=lambda dict :dict.get('age'),reverse=True)
# print(list1)

# print('abc'>'bba')

# class person:
#     __adress = 1
#     name = ''
#     age = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'我的名字是{self.name}年龄是{self.age}  {self.__adress}'
#     def __del__(self):
#         print('我被销毁了')
#     def dog(self):
#         print(f'我的名字是{self.name}年龄是{self.age}')
#     def cat(self):
#         print(f'我的名字是{self.name}年龄是{self.age}')
# lk = person('lk',20)
# print(lk.name)
class person:
    name = '12'

    def __init__(self, name):
        self.name = name
        print('父类构造方法执行了')

    def eat(self):
        print(f'{self.name}会吃东西')


class lk(person):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        print('子类构造方法执行了')

    def goshopping(self):
        print(f'{self.name}会购物')

# lk('liu',20).goshopping()

print(lk('liu',20).name)