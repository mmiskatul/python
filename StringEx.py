Username=input("Enter a userName : ")
if len(Username)>12 :
    print("Your user Name can't be more than 12 characters ")
elif not Username.find(" ") ==-1 :
    print("Your user name can't contain space")
elif not  Username.isalpha () :
     print("your user id can't contain digit")
else :
    print(f"Welcome {Username}")