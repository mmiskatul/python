unit=input("is this tempareture is celsius or fehrenheit (C or F ) :")
temp=float(input("enter the temperature : "))

if unit =="c" :
    temp=round(((temp*9)/5)+32,1)
    print(f"temperature is {round(temp,1)} F")
elif unit =="f" :
    temp =round(((temp-32)*5)/9,1)
    print(f"temperature is {round(temp,1)} C")
else :
    print (f"{unit} is invalid ")
 