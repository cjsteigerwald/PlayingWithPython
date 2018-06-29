#!/usr/bin/python

def main():
    write()
    append()
    read()

# write to file, if file exists truncates file / else file does
# not exist and creates new file
def write():
    # open a file for writing and create it if it does not exits
    f= open("guru99a.txt","w+")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    # close the file when done
    f.close()

# append to a file
def append():
    # open a file for writing and create it if it does not exits
    f= open("guru99a.txt","a+")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+11))
    # close the file when done
    f.close()

# read from a file and display to console
def read():
    f= open ("guru99.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)

if __name__ == "__main__":
    main()