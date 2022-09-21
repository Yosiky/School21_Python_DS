import timeit
import random
from collections import Counter

def create_dict(arg):
    res = {i : 0 for i in range(101)}
    for i in arg:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

def find_top(arg):
    ee_dict = create_dict(arg)
    return dict(sorted(list(zip(ee_dict.keys(), ee_dict.values())),
        reverse=True, key=lambda x: (x[1], x[0]))[:10])

def test(func, par, count):
    return timeit.timeit(lambda: func(par), number=count)

if __name__ == '__main__':
    try:
        count = 1000000
        list_some = [random.randrange(101) for i in range(1000000)]
        print(f'my function: {timeit.timeit(lambda: create_dict(list_some), number=count)}')
        print(f'counter: {timeit.timeit(lambda: Counter({list_some}), number=count)}')
        print(f'my function: {timeit.timeit(lambda: find_top(list_some), number=count)}')
        print(f'my function: {timeit.timeit(lambda: Counter({list_some}).most_common(10), number=count)}')
        
    except Exception as some:
        print(some)
