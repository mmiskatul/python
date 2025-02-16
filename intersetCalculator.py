principle =0
rate =0
time=0
while True :
    principle =float(input("Enter the Principle amout : "))
    if principle <0 :
        print ("priciple is not less then or equal zero");
    else :
        break 
        
while True :
    rate =float(input("Enter the Rate  : "))
    if rate <0 :
        print ("Interst Rate can't be less then or equal zero");
    else :
        break;
    
while True :
    time =int(input("Enter the time in year : "))
    if time <0 :
        print ("Time is not less then or equal zero");
    else :
        break
    
result=principle* pow((1+(rate/100 )),time)
print(f" Balance after {time} year is : ${result} ");