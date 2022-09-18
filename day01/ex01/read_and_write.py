

def change(str):
    line = str.split('"')
    res = ""
    for i in range(len(line)):
        if i % 2 == 1:
            res += '"' + line[i] + '"'
        else:
            res += '\t'.join(line[i].split(','))   
    return res

def copy_in_file(dst, src, func=None):
    data = src.readlines()
    for i in data:
        dst.write(func(i))

if __name__ == '__main__':
    with open('ds.csv', "r") as file_input:
        with open('ds.tsv', "w") as file_output:
            copy_in_file(file_output, file_input, change)
