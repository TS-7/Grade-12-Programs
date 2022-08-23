''' Program 4: WAP to read a text file line by line and display each word seperated with a # '''

def txt():
    f = open("smack.txt", "r+")
    for i in f.readlines():
        for j in i:
            if j == ' ':
                print('#', end='')
                continue
            print(j, end='')
    f.close()

txt()

''' SAMPLE OUTPUT REMINDER. LEFT SIDE OF THE RECORD '''