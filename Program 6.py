''' PROGRAM 6: WAP to copy all the lines that contains char 'a' in a  file and write it to another file '''

def copy():
    f = open("smack.txt", "r+")
    for i in f.readlines():
        if 'a' in i:
            f = open("smack(c).txt", "w+")
            f.writelines(i)
    print("Successfully copied the required lines into a new file")
    f.close()
    
copy()

''' SAMPLE OUTPUT REMINDER LEFT SIDE OF THE RECORD PLS '''