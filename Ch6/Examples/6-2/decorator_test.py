def funA(fn):
    print('A')
    fn()            # 执行传入的fn参数
    return 'fkit'

'''
下面的装饰效果相当于funA(funB)
funB将会被替换（装饰）成该语句的返回值
由于funA函数返回fkit，因此funB就是fkit
'''
@funA
def funB():
    print('B')
print(funB)         # fkit
