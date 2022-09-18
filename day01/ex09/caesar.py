import sys

def code_char(x, shift, arr):
    x = chr(x)
    if x in arr:
        return arr[(ord(x) - ord('a') + shift) % 26]
    return x

def code_str(line, shift):
    arr_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    arr_upper = list(map(lambda x: x.upper(), arr_lower))
    res = ""
    for i in range(len(line)):
        if chr(line[i]).isupper():
            res += code_char(line[i], shift, arr_upper)
        else:
            res += code_char(line[i], shift, arr_lower)
    return res
    

if __name__ == '__main__':
    count = len(sys.argv)
    if count == 4:
        sys.argv[2] = sys.argv[2].encode('ascii')
        shift = int(sys.argv[3])
        arr_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        arr_upper = list(map(lambda x: x.upper(), arr_lower))
        start_lower = ord('a')
        start_upper = ord('A')
        match sys.argv[1].strip().lower():
            case 'encode':
                print(code_str(sys.argv[2], shift))
            case 'decode':
                print(code_str(sys.argv[2], -shift))
            case _:
                raise Exception("Not valid command")
    
    else:
        raise Exception("Not valid count arguments")


