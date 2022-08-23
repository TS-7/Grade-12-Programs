''' PROGRAM 8: WAP to search the records in binary file '''

import pickle
def search():
    f = open("smack.dat", "rb")
    rea = pickle.load(f)
    res = 0
    inp = int(input("Enter the roll number you want to search for: "))
    for i in rea:
        if inp == i[0]:
            print('Record Found!')
            print("Name of student: ",i[1])
            print("Marks of student: ",i[2])
            res += 1
            break
    if res == 0:
        print("No records found")
    f.close()

search()
    