# file = open('G:\Desktop\时间表.txt','a',encoding='utf-8')
# file.write('test/n')
# file.close()
import json
# with open('G:\Desktop\时间表.txt',encoding='utf-8') as file:
#     # file.write('123')
#     print(file.readline())
my_list = [('admin', '123456', '登录成功'), ('root','123456', '登录失败'), ('admin', '123123', '登录失败')]
with open('G:\Desktop\info.json','w',encoding='utf-8') as file:
    json.dump(my_list, file, ensure_ascii=False,indent=4)