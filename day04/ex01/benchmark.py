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

def func_three(arg, n):
    res = arg * n
    return list(map(lambda x: x if x.find("@gmail.com") else None, res))


if __name__ == '__main__':
    count = 90000000
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
            'anna@live.com', 'philipp@gmail.com']
    func = [func_one, func_two, func_three]
    res = list(map(lambda x: timeit.timeit(lambda: x(emails, 5), number=count), func))
    print('it is better to use a ', end='')
    if res[0] > res[1] and res[2] > res[1]:
        print('list comprehension')
    elif res[1] > res[0] and res[2] > res[0]:
        print('loop')
    else:
        print('map')
    res.sort()
    print(' vs '.join(list(map(str, res))))
