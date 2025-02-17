# employees=["Miskat","Nadim","Liza","mohammod","jannat","kafia","sami","Sathi"]
# txt_data="I like pizza! "
# file_path="output.txt"
# try: 
#     with open(file=file_path,mode="a") as file:
#         for employe in employees :
#             file.write("\n"+employe)
#         print(f"text file '{file_path}' create successfully")
# except FileExistsError:
#     print("this file already exists!")



# import json
# employees={
#      "name":"Miskat",
#      "age":22,
#      "job":"Cook",
     
     
# }
# file_path="output.json"
# try: 
#     with open(file=file_path,mode="a") as file:
#         json.dump(employees,file,indent=4)
#         print(f"json file '{file_path}' create successfully")
# except FileExistsError:
#     print("this file already exists!")

# csv
import csv
employees=[
            ["Name","age","job"],
           ["Miskat",22,"bekar"],
           ["mohammod",22,"DSA expart"],
           ["Liza",21,"profesional Web developer"]
           ]
file_path="output.csv"
try: 
    with open(file=file_path,mode="a",newline="") as file:
       writer=csv.writer(file)
       for row in employees :
           writer.writerow(row)
       print(f"Csv file '{file_path}' create successfully")
except FileExistsError:
    print("this file already exists!")