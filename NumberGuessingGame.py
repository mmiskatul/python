import random


lowest_num=1
higest_num=100
answer=random.randint(lowest_num,higest_num)

guecces=0
is_running =True
print("Python Number gueccing game")
print(f"Select a Number between {lowest_num} and {higest_num} ")

while is_running :
    guess=input("Enter your Guess :")
    if guess.isdigit() :
        guess=int(guess)
        guecces+=1
        if guess<lowest_num or guess>higest_num :
            print("that number is out of range")
            print(f"Please Select a Number between {lowest_num} and {higest_num} ")
        elif guess<answer:
            print("To low ")
        elif guess>answer :
            print("Too High ! Try again")
        else:
            print(f"Correct !The answer was {answer}")
            print(f"Number of guecces {guecces}")
            is_running=False
    else :
        print("Invalid guess")
        print(f"Please Select a Number between {lowest_num} and {higest_num} ")