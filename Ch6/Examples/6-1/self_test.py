class User:
    def test(self):
        print("self参数：", self)


u = User()
# 以方法形式调用test()方法
u.test()        # self参数：<__main__.User object at 0x……>
# 将User对象的test方法赋值给foo变量
foo = u.test
# 通过foo变量（函数形式）调用test()方法
foo()           # self参数：<__main__.User object at 0x……>
