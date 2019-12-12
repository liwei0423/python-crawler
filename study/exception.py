def diyException(level):
    if level > 0:
        raise Exception("raise exception", level)  # 主动抛出一个异常，并且带有参数
        print('我是不会执行的')  # 这行代码不会执行


try:
    diyException(2)  # 执行异常方法
except Exception as err:  # 捕获异常
    print(err)  # 打印异常参数

# 输出
('raise exception', 2)