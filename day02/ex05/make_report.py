from config import num_of_steps
from analytics import *
import sys

if __name__ == '__main__':
    try:
        count = len(sys.argv)
        if count == 2:
            a = Research('data.csv')
            arr = a.file_reader()
            c = Analitics(arr)
            print(arr)
            res = c.counts()
            print(f"{res[0]} {res[1]}")
            res = c.fractions(res[0], res[1])
            print(f"{res[0]} {res[1]}")
            print(c.predict_random(num_of_steps))
            res = c.predict_last()
            print(f"{res[0]} {res[1]}")
        else:
            raise Exception("No valid count argument")
    except Exception as some:
        print(some)
