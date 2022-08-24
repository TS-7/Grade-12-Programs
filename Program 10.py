''' PROGRAM 10: Create a binary file which cotains the students details and to search the
particular student based on roll no and display the details '''

import pickle

def writeb():
    f = open ("smack.dat","wb+")
    record = []
    while True:
        rno = int(input("Enter roll no: "))
        name = str(input("Enter name: "))
        marks = int(input("Enter marks: "))
        data = [rno, name, marks]
        record.append(data)
        ch= str(input("Would you like to enter more records: "))
        if ch == 'yes':
            pass
        elif ch == 'no':
            break
        elif (ch != 'yes' and ch != 'no'):
            print("Invalid input")
            break 
    pickle.dump(record, f)
    f.close()

writeb()

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
