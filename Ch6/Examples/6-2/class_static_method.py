class Bird:
    # 使用@classmethod修饰的方法是类方法
    @classmethod
    def fly(cls):
        print("类方法fly: ", cls)
    # 使用@staticmethod修饰的方法是静态方法

    def info(p):
        print("静态方法info: ", p)


# 调用类方法，Bird类会自动绑定到第一个参数
Bird.fly()              # 类方法fly: <class '__main__.Bird'>
# 调用静态方法，不会自动绑定，因此需要手动绑定第一个参数
Bird.info("crazyit")    # 静态方法info: crazyit

# 创建Bird对象
b = Bird()
# 使用对象调用fly()类方法，第一个参数被自动绑定到Bird类
b.fly()                 # 类方法fly: <class '__main__.Bird'>
# b.info("fkit")        # TypeError: info() takes 1 positional argument but 2 were given
b.info()                # 静态方法info: <__main__.Bird object at 0x......>
