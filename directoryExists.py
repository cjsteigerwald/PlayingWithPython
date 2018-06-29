#!/usr/bin/python

# https://docs.python.org/3/library/os.html
import os.path
# https://docs.python.org/2/library/os.path.html
from os import path
# in python 3.4 and later can import pathlib and use it
#import pathlib

def main():
    targetDirectory = '/home/cs741q/Documents'
    targetFile = 'guru99.txt'
    pathExists(targetDirectory, targetFile)
    isFile(targetDirectory, targetFile)
    isDir(targetDirectory, targetFile)
    # path() uses pathlib from python 3.4
    #path(targetDirectory, targetFile)

# if directory or file exists return true, else false
def pathExists(testDirectory, testFile):
    print("file exist: " + str(path.exists(testFile)))
    print("file exist: " + str(path.exists('career.guru99.txt')))
    print("file exist: " + str(path.exists(testDirectory)))

# if file exists return true, else false
def isFile(testDirectory, testFile):
    print("Is it a File? " + str(path.isfile(testFile)))
    print("Is it a File? " + str(path.isfile(testDirectory)))

# if directory exists return true, else false
def isDir(testDirectory, testFile):
    print ("Is it Directory?" + str(path.isdir(testFile)))
    print ("Is it Directory?" + str(path.isdir(testDirectory)))

# use path lib to determine if file exists return true, else false
"""
def path(testDirectory, testFile):
    if testFile.exists():
        print("File exist")
    else:
        print("File does not exist")
"""
if __name__ == "__main__":
    main()