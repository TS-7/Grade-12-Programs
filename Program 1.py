''' PROGRAM 1 : Write a program ot print the fibonacci series using function '''

n = int(input("Enter the number of times you want to loop through the fibbonacci series: "))

def fibb(n):
    f = 1
    s = 1
    i = 0
    if n <= 0:
        print("Invalid value")
    while i < n:
        print(f)
        f,s = s, f+s
        i += 1
fibb(n)

''' Left side of the record, sample output needs to be written. Write it as it is on the console. Example only for the first program below, I'll add reminders
for the rest.

If you can't follow the same for the rest of the programs, you really need to consider quitting <3 '''

''' SAMPLE OUTPUT EXAMPLE [ WRITE IT ON THE BLOODY LEFT SIDE ] '''

'''

Enter the number of times you want to loop through the fibonacci series: 5
1
1
2
3
5

'''