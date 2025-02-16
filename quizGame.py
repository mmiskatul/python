questions = ("How many element in the priodic table ? :",
            "which animal lays the largest Eggs? :",
            "what is the most abundant gas in the earth's Atomosphere? :",
            "How many bones are in the Human Body? :",
            "Which planet in the Solar system is the Hottest ?: ")

options =(("A. 116","B. 117","C. 118","D. 119"),
         ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
         ("A. Nitrogen","B. Oxygen","C. carbon_dioxide","D. Hydrogen"),
         ("A. 209","B. 205","C. 206","D. 207"),
         ("A. Mercury","B. Venus","C. Earth","D. March"))
answers=("C" ,"D","A","C","B")
guesses=[]
score = 0
question_num =0

for question in questions :
    print("---------------------------")
    print(question)
    for option in options[question_num] :
        print(option)
    
    quess=input("Enter (A ,B ,C ,D ) : ").upper()
    guesses.append(quess)
    if quess==answers[question_num] :
        score+=1
        print("CORRECT !")
    else :
        print("INCORRECT !")
        print(f"{answers[question_num]} is the the correct Answer ")
    question_num+=1
    

print("---------------------------")
print("        YOUR RESULT        ")
print("---------------------------")


print("Answers : ",end="")
for answer in answers :
    print(answer,end=" ")
print()
print("Guesses: ",end="")
for guess in guesses :
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)

print(f"Your Score is :{score}%")
