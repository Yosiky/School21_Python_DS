import timeit
import sys

def func_one(arg):
    new_list = []
    for i in arg:
        if i.find('@gmail.com') != -1:
            new_list.append(i)
    return new_list

def func_two(arg):
    return [i for i in arg if i.find('@gmail.com') != -1]

def func_three(arg):
    return list(map(lambda x: x if x.find("@gmail.com") else None, arg))

def func_four(arg):
    return list(filter(lambda x: x.find("@gmail.com") != -1, arg))

def test(func, n):
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
            'anna@live.com', 'philipp@gmail.com'] * 5
    return timeit.timeit(lambda: func(emails), number=n)

if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            res = int(sys.argv[2])
            speed = 0
            if sys.argv[1] == 'list_comprehension':
                speed = test(func_two, res)
            elif sys.argv[1] == 'loop':
                speed = test(func_one, res)
            elif sys.argv[1] == 'map':
                speed = test(func_three, res)
            elif sys.argv[1] == 'filter':
                speed = test(func_four, res)
            print(speed)
        else:
            Exception("not valid count arguments")
    except Exception as some:
        print(some)
