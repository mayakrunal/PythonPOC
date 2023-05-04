def create_cubes(n):
    for num in range(n):
        yield num ** 3


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def simple_gen():
    for x in range(3):
        yield x


if __name__ == '__main__':
    # for x in create_cubes(500):
    #     print(x)

    # for x in gen_fibon(10):
    #     print(x)
    g = simple_gen()
    print(next(g))
    print(next(g))
    print(next(g))

    s = 'hello'

    s_iter = iter(s)

    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
