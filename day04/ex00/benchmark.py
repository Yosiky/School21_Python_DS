import timeit

def func_one(arg, n):
    res = arg * n
    new_list = []
    for i in res:
        if i.find('@gmail.com') != -1:
            new_list.append(i)
    return new_list

def func_two(arg, n):
    res = arg * n
    return [i for i in res if i.find('@gmail.com') != -1]

if __name__ == '__main__':
    count=1000000
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
            'anna@live.com', 'philipp@gmail.com']
    first = timeit.timeit(lambda: func_one(emails, 5), number=count)
    second = timeit.timeit(lambda: func_two(emails, 5), number=count)
    print('it is better to use a ', end='')
    if first > second:
        print('list comprehension')
    else:
        print('loop')
    res = sorted([first, second])
    print(f"{res[0]} {res[1]}")
