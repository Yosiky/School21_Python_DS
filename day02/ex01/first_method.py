
class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            lines = file.readlines()
            for i in lines:
                print(i, end='')
        return lines

if __name__ == '__main__':
    a = Research()
    a.file_reader()

