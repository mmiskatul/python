weight=float(input("Enter your Weight : "))
unit=input("Kilogram or Pounds (K or l)")
if unit =="k" :
    weight *=2.205
    unit="Lbs"
    print(f"your weight is : {round(weight,1)} {unit}")
elif unit =="l" :
    weight /=2.205
    unit ="kg"
    print(f"your weight is : {round(weight,1)} {unit}")
else :
    print (f"{unit} was not valid")
    
    
