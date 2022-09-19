import sys

class Research:
    def __init__(self, file_name=None):
        self._file_name = file_name

    def file_reader(self):
        with open(self._file_name, 'r') as file:
            lines = file.readlines()
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
