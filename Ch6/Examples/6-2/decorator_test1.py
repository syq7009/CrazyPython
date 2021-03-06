def foo(fn):
    # 定义一个嵌套函数
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n - 1))
        # 查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print("*" * 15)
        return fn(n * (n - 1))
    return bar


'''
下面的装饰效果相当于foo(my_test)
my_test将会被替换（装饰）成该语句的返回值
由于foo()函数返回bar函数，因此my_test就是bar
'''


@foo
def my_test(a):
    print("==my_test函数==", a)


# 打印my_test函数，将看到实际上是bar函数
print(my_test)          # <function foo.<locals>.bar at 0x......>
# 下面的代码看上去是调用my_test()函数，其实是调用bar()函数
my_test(10)
my_test(6, 5)
