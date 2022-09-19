
class Must_read:
    with open('data.csv', 'r') as file:
        for i in file.readlines():
            print(i, end='')

if __name__ == '__main__':
    Must_read


