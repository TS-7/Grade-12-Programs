''' PROGRAM 7: WAP to write student record into binary file '''
import pickle

def writeb():
    f= open ("smack.dat","wb+")
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

''' FRIENDLY REMINDER TO WRITE THE SAMPLE OUTPUT ON THE LEFT SIDE OF THE RECORD '''