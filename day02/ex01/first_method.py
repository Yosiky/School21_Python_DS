
class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            lines = file.read()
            print(lines, end='')
        return lines

if __name__ == '__main__':
    a = Research()
    a.file_reader()

