class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    @classmethod
    def run(cls,speed):
        print(cls.name,speed,'行驶')
# 访问方式1
c = Car("宝马")
c.run("100迈")
# 访问方式2
Car.run("100迈")