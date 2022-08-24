''' PROGRAM 8: WAP to search the records in binary file '''

import pickle
def searchb():
    stu = {}
    found = False
    f = open('smack.dat', 'rb+')
    srch = int(input("Enter the roll number you want to search: "))
    search = [srch]

    try:
        print('Searching the binary for roll no.', srch)
        while True:
            stu = pickle.load(f)
            if stu['Rollno'] in search:
                print(f"Student Name: {stu['Name']}\nStudent Marks: {stu['Marks']}")
                found = True
    except EOFError:
        if found == False:
            print("No records found with the given values")
        f.close()
        
searchb()        

''' FRIENDLY REMINDER TO WRITE SAMPLE OUTPUT - LEFT SIDE OF THE RECORD '''
