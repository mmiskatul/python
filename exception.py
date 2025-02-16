try:
    num=int(input("Enter a number : "))
    print( 1 / num )
except ZeroDivisionError :
    print("You can't divide by Zero ")
except ValueError :
    print("You enter a invalid value ")
except Exception:
    print("Somthing Went wrong !")
    