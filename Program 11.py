''' PROGRAM 11: Create the binary which contains the student details and to update the particular student based on roll no. '''

import pickle

def test():
    f = open("smack.dat", "rb+")
    r = int(input("Enter the roll number you want to update: "))
    try:
        while True:
            pos = f.tell()
            rec = pickle.load(f)
            if rec[0] == r:
                mark = int(input("Enter the marks you want to update for this user: "))
                rec[2] = mark
                f.seek(pos)
                pickle.dump(rec, f)
            else:
                print("No records found.")
    except EOFError:
        f.close()

test()

def read():
    f = open ("smack.dat","rb+")
    try:
        while True:
            rec = pickle.load(f)
            print(rec)
    except EOFError:
        f.close()

read()

def update():
    f = open("smack.dat", "rb")
    r = int(input("Enter the roll number you want to update"))
    b = pickle.load(f)
    found = 0
    for i in b:
        if r == i[0]:
            mark = int(input("Enter the marks you want to update for this user: "))
            i[2] == mark
            found = 1
            break

    if found == 0:
        print("Records not found")
        f.close()
    else:
        f2 = open("smack.dat", "wb")
        f2.seek(0)
        pickle.dump(b, f2)
        f2.close()

''' FRIENDLY REMINDER TO WRITE THE SAMPLE OUTPUT ON THE LEFT SIDE OF THE RECORD '''
