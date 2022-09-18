
def data_types():
    res = map(type, [1, 'str', 1.1, True, [1, 1, 1], {1:'hello'}, (1, 1, 1), {1, 1, 1}])
    print('[{0}]'.format(', '.join(i.__name__ for i in res)))

if __name__ == '__main__':
    data_types()
