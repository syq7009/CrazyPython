class Person:
    '这是学习Python定义的一个Person类'
    # 下面定义了一个类变量
    hair = 'black'

    def __init__(self, name='Charlie', age=8):
        # 下面为Person对象增加两个实例变量
        self.name = name
        self.age = age

    # 下面定义了一个say方法
    def say(self, content):
        print(content)


# 调用Person类的构造方法，返回一个Person对象
# 将该Person对象赋值给p变量
p = Person()
# 输出p的name、age实例变量
print(p.name, p.age)        # Charlie 8
# 通过p的name实例变量，直接为该实例变量赋值
p.name = '李刚'
# 调用p的say()方法，在声明say()方法时定义了两个形参
# 但第一个形参（self）时自动绑定的，因此调用该方法只需为第二个形参指定一个值
p.say('Python语言很简单，学习很容易')
# 再次输出p的name、age实例变量
print(p.name, p.age)        # 李刚 8

# Python语言可以为对象动态增加实例变量——只要为它的新变量赋值值即可
# 为p对象增加一个skills实例变量
p.skills = ['programming', 'swimming']
print(p.skills)
# Python语言可以动态删除对象的实例变量——使用del语句即可
# 删除p对象的name实例变量
del p.name
# 再次访问p的name实例变量将出错
# print(p.name)               # AttributeError

# Python语言也允许为对象动态增加方法，但不会自动将调用者自动绑定到第一个参数
# （即使将第一个参数命名为self也没用）。
# 先定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对p的foo方法赋值（动态增加方法）
p.foo = info
# Python不会自动将调用者绑定到第一个参数
# 因此程序需要手动将调用者绑定到第一个参数
p.foo(p)
# 使用lambda表达式为p对象的bar方法赋值（动态增加方法）
p.bar = lambda self: print("---lambda表达式---", self)
p.bar(p)

# 如果希望动态增加的方法也能自动绑定到第一个参数上，
# 则可借助于types模块的MethodType进行包装
def intro_func(self, content):
    print("我是一个人，信息为：%s" % content)
# 导入MethodType
from types import MethodType
# 使用MethodType对intro_func进行包装，将该函数第一个参数绑定为p
p.intro = MethodType(intro_func, p)
p.intro("生活在别处")
