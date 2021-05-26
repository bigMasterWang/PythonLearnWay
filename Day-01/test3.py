# closure
# we have a closure in Python when a nested function references a value in its enclosing scope.
# 嵌套函数能够使用封闭函数中的变量

def print_meg(msg):
    # this is outer enclosing function
    def printer():
        # this is nested function
        print(msg)
    printer()


print_meg("hello world")


def print_msg_two(msg):
    def printer():
        print(msg)

    return printer

another = print_msg_two("hello world two")
another()
del print_msg_two
another()

# 根据上面的代码
# This technique by which some data ("Hello") gets attached to the code is called closure in Python.
#
# This value in the enclosing scope is remembered even when the variable goes out of scope
# or the function itself is removed from the current namespace.
#
#
# The criteria that must be met to create closure in Python are summarized in the following points.
#
# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.
#
# When to use closures?
# So what are closures good for?
#
# Closures can avoid the use of global values and provides some form of data hiding.
# It can also provide an object oriented solution to the problem.

def make_multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier

time3 = make_multiplier_of(3)

time5 = make_multiplier_of(5)

print(time3(9))
print(time5(9))
print(time3(time5(3)))


# All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function.
# Referring to the example above, we know times3 and times5 are closure functions.

# 3
print(time3.__closure__[0].cell_contents)
print(time5.__closure__[0].cell_contents)
# None
print(make_multiplier_of.__closure__)