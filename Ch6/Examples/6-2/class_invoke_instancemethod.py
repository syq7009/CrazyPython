class User:
    def walk(self):
        print(self, "正在慢慢地走")

# 通过类调用实例方法
# User.walk()         # TypeError: walk() missing …… argument: 'self'

# 可显式地为方法的第一个参数绑定参数值
u = User()
User.walk(u)        # <__main__.User object at 0x……> 正在慢慢地走

# 显式地为方法的第一个参数绑定字符串参数值
User.walk('fkit')   # fkit 正在慢慢地走
