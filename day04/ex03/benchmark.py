import timeit
import sys
from functools import reduce

def func_one(arg):
    res = 0
    for i in range(arg + 1):
        res = res + i * i
    return res

def func_two(arg):
    return reduce(lambda x, y: x + y, range(arg + 1))

def test(func, par, count):
    return timeit.timeit(lambda: func(par), number=count)

if __name__ == '__main__':
    try:
        if len(sys.argv) == 4:
            speed = 0
            if sys.argv[1] == 'loop':
                speed = test(func_one, int(sys.argv[3]), int(sys.argv[2]))
            elif sys.argv[1] == 'reduce':
                speed = test(func_two, int(sys.argv[3]), int(sys.argv[2]))
            print(speed)
        else:
            Exception("not valid count arguments")
    except Exception as some:
        print(some)
