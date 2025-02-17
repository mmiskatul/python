# file_path="C:/Users/user/Desktop/output.txt"
# try :
#     with open(file_path,"r")as file:
#         content=file.read()
#         print(content)
# except FileNotFoundError :
#     print("file is not found")
# except PermissionError :
#     print("you don't have permision to read the file!")

# # json
# import json
# file_path="C:/Users/user/Desktop/output.json"
# try :
#     with open(file_path,"r")as file:
#         content=json.load(file) 
#         print(content)
# except FileNotFoundError :
#     print("file is not found")
# except PermissionError :
#     print("you don't have permision to read the file!")

# Csv
import csv
file_path="C:/Users/user/Desktop/output.csv"
try :
    with open(file_path,"r")as file:
        content=csv.reader(file)
        for line in content:
             print(line)
except FileNotFoundError :
    print("file is not found")
except PermissionError :
    print("you don't have permision to read the file!")

