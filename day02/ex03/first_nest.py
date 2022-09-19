import sys

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
    def counts(self, arr):
        return sum(map(lambda x: x[0], arr)), sum(map(lambda x: x[1], arr))

    def fractions(self, head, tail):
        s = head + tail
        return head / s * 100, tail / s * 100
            

if __name__ == '__main__':
    try:
        count = len(sys.argv)
        if count == 2:
            a = Research('data.csv')
            c = Calculations()
            arr = a.file_reader()
            print(arr)
            res = c.counts(arr)
            print(f"{res[0]} {res[1]}")
            res = c.fractions(res[0], res[1])
            print(f"{res[0]} {res[1]}")
            
        else:
            raise Exception("No valid count argument")
    except Exception as some:
        print(some)
