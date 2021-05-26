async def async_foo():
    print("do something asynchronously here...")

def bar():
    async_foo()


bar()