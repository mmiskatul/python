import os
file_path="Test.txt"

if os.path.exists(file_path):
    print(f"the logication '{file_path}' Exists ")
    if os.path.isfile(file_path):
        print("this is a file")
    elif os.path.isdir(file_path):
        print("this is a Directory ")
else :
    print("that loctaion doesn't exists")
