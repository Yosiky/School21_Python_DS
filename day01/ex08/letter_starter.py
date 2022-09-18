import sys

def get_welcom_letter(email):
    with open('employees.tsv', 'r') as file_input:
        lines = [i.strip().split('\t') for i in file_input.readlines()]
        for i in lines[1:]:
            if i[2] == email:
                return f"Dear {i[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires."
    return None

if __name__ == '__main__':
    count = len(sys.argv)
    if count == 2:
        print(get_welcom_letter(sys.argv[1]))
    else:
        print('No valid count argument')
