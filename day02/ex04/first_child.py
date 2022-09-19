import sys
from random import randint

class Research:
    def __init__(self, file_name=None):
        self._file_name = file_name

    def file_reader(self, has_header=True):
        def check_lines(arr):
            for i in lines[1:]:
                if i[0:3] != '0,1' and i[0:3] != '1,0':
                    raise Exception("Not valid line in file")

        with open(self._file_name, 'r') as file:
            lines = file.readlines()
            if has_header:
                if len(lines[0].split(',')) == 2:
                    check_lines(lines[1:])
                else:
                    raise Exception("Not valid header in file")
                lines = lines[1:]
            else:
                check_lines(lines)

        return list(map(lambda x: list(map(int, x.split(','))), lines))

class Calculations:
    def __init__(self, arg):
        self._data = arg

    def counts(self):
        self._count_head = sum(map(lambda x: x[0], self._data))
        self._count_tail = sum(map(lambda x: x[1], self._data))
        return self._count_head, self._count_tail

    def fractions(self, head, tail):
        s = head + tail
        return head / s * 100, tail / s * 100
           
class Analitics(Calculations):
    def __init__(self, arg):
        super().__init__(arg)

    def predict_random(self, count):
        res = []
        for i in range(count):
            value = randint(0, 1)
            res.append([value, abs(value - 1)])
        return res

    def predict_last(self):
        return self._data[-1]
    

if __name__ == '__main__':
    try:
        count = len(sys.argv)
        if count == 2:
            a = Research('data.csv')
            arr = a.file_reader()
            c = Analitics(arr)
            print(arr)
            res = c.counts()
            print(f"{res[0]} {res[1]}")
            res = c.fractions(res[0], res[1])
            print(f"{res[0]} {res[1]}")
            print(c.predict_random(3))
            res = c.predict_last()
            print(f"{res[0]} {res[1]}")
            
        else:
            raise Exception("No valid count argument")
    except Exception as some:
        print(some)
