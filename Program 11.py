''' PROGRAM 11: Create the binary which contains the student details and to update the particular student based on roll no. '''

import pickle

def update():
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

update()

def read():
    f = open ("smack.dat","rb+")
    try:
        while True:
            rec = pickle.load(f)
            print(rec)
    except EOFError:
        f.close()

read()

''' FRIENDLY REMINDER TO WRITE THE SAMPLE OUTPUT ON THE LEFT SIDE OF THE RECORD '''
