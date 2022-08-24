''' PROGRAM 7: WAP to write student record into binary file '''
import pickle

def writeb():
    f= open ("smack.dat","wb")
    record = {}
    ch = 'yes'
    while True:
        rno = int(input("Enter roll no: "))
        name = str(input("Enter name: "))
        marks = int(input("Enter marks: "))
        record['Rollno'] = rno
        record['Name'] = name
        record['Marks'] = marks
        pickle.dump(record ,f)
        ch = input("Would you like to enter more records: ")
        if ch=='no':
            break
        elif (ch != 'yes' and ch != 'no'):
            print("Invalid input")
            break 
    f.close()

''' FRIENDLY REMINDER TO WRITE THE SAMPLE OUTPUT ON THE LEFT SIDE OF THE RECORD '''
