def show_Balance(balance):
    print(f"\nYour balance is ${balance:.2f}")
def deposit():
    amout=float(input("Enter an amount to be deposited : "))
    if amout<0 :
        print("That's not a valid amount")
        return 0
    else:
        return amout
def withdraw(balance):
    amout=float(input("Enter an amout to be Withdraw : "))
    if amout>balance :
        print("Insufficient Balance ")
        return 0
    elif amout<0 :
        print("That's a inavlid amount ")
        return 0;
    else :
        return amout
def main():
    balance=0
    is_running=True

    while is_running :
        print("\n*********************")
        print ("Banking Program ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice=input("\nEnter the your choice of  operation(1-4) : ")
        
        if choice=="1" :
            show_Balance(balance);
        elif choice=="2" :
            balance += deposit();
        elif choice=="3":
            balance -= withdraw(balance);
        elif choice=="4":
            print("\n\nThank you for using our program ")
            is_running=False
        else :
            print(f"{choice}is not a valid choice ! Try again ")
    
    print("Thank you ! Have a nice day !")     
    

if __name__ =='__main__':
    main()
    