import sys

class Research:
    def __init__(self, file_name=None):
        self._file_name = file_name

    def file_reader(self):
        with open(self._file_name, 'r') as file:
            lines = file.readlines()
            if len(lines[0].split(',')) == 2:
                for i in lines[1:]:
                    if i[0:3] != '0,1' and i[0:3] != '1,0':
                        raise Exception("Not valid line in file")
            else:
                raise Exception("Not valid header in file")
            for i in lines:
                print(i, end='')
        return lines

if __name__ == '__main__':
    try:
        count = len(sys.argv)
        if count == 2:
            a = Research('data.csv')
            a.file_reader()
        else:
            raise Exception("No valid count argument")
    except Exception as some:
        print(some)
