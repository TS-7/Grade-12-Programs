''' PROGRAM 11: Create the binary which contains the student details and to update the particular student based don roll no. '''

import pickle

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
        else:
            print("No updates made found.")

    if found == 0:
        print("Records not found")
    else:
        f.seek(0)
        pickle.dump(b, f)

    f.close()

update()
''' FRIENDLY REMINDER TO WRITE THE SAMPLE OUTPUT ON THE LEFT SIDE OF THE RECORD '''
