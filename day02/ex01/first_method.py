
class Research:
    def file_reader():
        with open('data.csv', 'r') as file:
            for i in file.readlines():
                print(i, end='')


if __name__ == '__main__':
    a = Research
    a.file_reader()

