import sys

def parse_email(str):
    email = str
    [name, surname] = str.split('@', 1)[0].split('.')
    name = name[0].upper() + name[1:].lower()
    surname = surname[0].upper() + surname[1:].lower()
    return [name, surname, email]

if __name__ == '__main__':
    count = len(sys.argv)
    if count == 2:
        with open(sys.argv[1], 'r') as file_input:
            with open('employees.tsv', 'w') as file_output:
                file_output.write(f'"Name"\t"Surname"\t"E-mail"\n')
                for i in file_input.readlines():
                    [name, surname, email] = parse_email(i.strip())
                    file_output.write(f'{name}\t{surname}\t{email}\n')
    else:
        print('No valid count arguments')
