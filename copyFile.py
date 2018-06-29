#!/usr/bin/python

# https://docs.python.org/3/library/os.html
import os
# https://docs.python.org/2/library/shutil.html
import shutil
# https://docs.python.org/2/library/os.path.html
from os import path
# https://docs.python.org/2/library/datetime.html
import datetime
from datetime import date, time, timedelta
# https://docs.python.org/2/library/time.html
import time

def main():
    original_file = "guru99.txt"
    if path.exists(original_file):
        make_duplicate_file(original_file)

# make a duplicate of an existing file
def make_duplicate_file(original_file):
    # get path to original_file
    original_file_path = path.realpath("guru99.txt")

    # separate the path from the filter
    file_path, file_name = path.split(original_file_path)
    print("path: " + file_path)
    print("file: " + file_name)

    # make a backup copy by appending "bak" to the name
    destination_file_path = original_file_path + ".bak"
    # using the shell to make a copy of the file, shutil.copy() does not include meta-data 
    shutil.copy(original_file_path, destination_file_path)
    # use shutil.copystat() to include all meta-data i.e.: file permissions, modification time, and etc 
    shutil.copystat(original_file_path, destination_file_path)

    # get modification time
    modification_time = time.ctime(path.getmtime(destination_file_path))
    print(modification_time)
    print(datetime.datetime.fromtimestamp(path.getmtime(destination_file_path)))

if __name__ == "__main__":
    main()