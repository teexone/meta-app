from malevich.square import processor, DF


@processor()
def hello(some_data: DF) -> DF:
    return some_data.insert(-1, "hello", "world")