# coding=utf-8
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


human = Celsius(36)

human.temperature = 37

print(human.temperature)

print(human.to_fahrenheit())

# Whenever we assign or retrieve any object attribute like temperature as shown above,
# Python searches it in the object's built-in __dict__ dictionary attribute.
print(human.__dict__)


# python standard private variables

class CelsiusTwo:

    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_tempreature() * 1.8) + 32

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    def get_tempreature(self):
        return self._temperature


human2 = CelsiusTwo(37)
print(human2.get_tempreature())
print(human2.to_fahrenheit())

# human2.set_temperature(-300)
print(human2.to_fahrenheit())

print(human2.__dict__)


# All in all, our new update was not backwards compatible. This is where @property comes to rescue.

class CelsiusThree:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Get Value...")
        return self._temperature

    def set_temperature(self, value):
        print("Set Value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possiable")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


human3 = CelsiusThree(300)

print(human3.__dict__)

# 所以说这是针对python3以上的
# 说白了 property(dget,fset,fdel,doc)这个类，就是给属性添加get，set关系的
# 第一个参数是get方法，第二个参数是set方法，第三个参数我也不清楚，第四个参数是说明
# 然后你去寻找实例的 __dict__ 里面，只有你在get，set里面设置的私有属性_variables
# 所以说这个方法不仅是修改了寻找属性的方式，从实例的__dict__里面找，改为了调用那两个方法
# 并且还把声明为property类的属性从实例的 __dict__ 里面给删除了
