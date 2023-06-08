print('导入包的时候会执行')
class t:
    def add(self,a,b):
        print(a+b)
        return a+b
    def prin(self,a,b):
        return print(a,b)
if __name__ == '__main__':
    print('导入包的时候不会执行')