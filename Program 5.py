''' PROGRAM 5: Read a text file and display the number of vowels / consonants / uppercase / lowercase characters in the file '''

def cnt():
    f=open("smack.txt","r+")
    v = ['a','e','i','o','u']
    vowels = 0
    cons = 0
    lowercase = 0
    uppercase = 0
    for ch in f.read():
        if (ch.islower()):
            lowercase += 1
        elif(ch.isupper()):
            uppercase += 1
        ch = ch.lower()
        if( ch in v ):
            vowels += 1
        else:
            cons += 1
    f.close()
    print("Vowels are : ",vowels)
    print("Consonants are : ",cons)
    print("Lower case letters are : ",lowercase)
    print("Upper case letters are : ",uppercase)      

cnt()

''' SAMPLE OUTPUT REMINDER FOLKS '''