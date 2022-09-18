
class Research:
    _file_name = None
    _fd_file = None
    _file_lines = None

    def __init__(self, file_name=None):
        self._file_name = file_name
        self._fd_file = open(file_name, 'r')

    def __del__(self):
        self._fd_file.close()

    def file_reader(self):
        self._file_lines = self._fd_file.readlines()
        return self._file_lines

if __name__ == '__main__':
    a = Research('data.csv')
    lines = a.file_reader()
    for i in lines:
        print(i, end='')

