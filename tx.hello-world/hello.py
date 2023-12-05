from malevich.square import processor, DF


@processor()
def hello(some_data: DF):
    return some_data.insert(-1, "hello", "world")

