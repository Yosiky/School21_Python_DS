def to_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return {i[0] : int(i[1]) for i in list_of_tuples}

if __name__ == '__main__':
    dictionary = to_dict()
    res = sorted(list(zip(dictionary.values(), dictionary.keys())), key=lambda x: (-x[0], x[1]))
    for i in res:
        print(f"{i[1]}")
    

