''' PROGRAM 2 : WAP to check whether a user input string is a palindrome or not 
[ WAP is Write A Program - I hope none of you are totally brain dead to read it as anything else. Not gonna repeat for rest of the programs ]'''

f = str(input("Enter the string you want to check for a palindrome: "))
def pali(f):
    if f[::-1] == f:
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")

pali(f)

''' SAMPLE OUTPUT REMINDER '''
