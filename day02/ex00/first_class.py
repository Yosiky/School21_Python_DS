
class Must_read:
    _file_name = None
    _fd_file = None
    _file_lines = None

    def __init__(self, file_name=None):
        self._file_name = file_name
        self._fd_file = open(file_name, 'r')

    def __del__(self):
        self._fd_file.close()

    def printlines(self):
        self._file_lines = self._fd_file.readlines()
        for i in self._file_lines:
            print(i, end='')

if __name__ == '__main__':
    a = Must_read('data.csv')
    a.printlines()


