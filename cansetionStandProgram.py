manu ={"Pizza":3.00,
       "Nachos":4.50,
       "popcorn":6.00,
       "frices":2.50,
       "chips":1.00,
       "pretzel":3.50,
       "Soda":3.00,
       "Lemonade":4.25}
cart=[]
total=0
print("------------THE MENU------------")
for key,value in manu.items():
    print(f"{key :10} :${value:.2f}")

print("--------------------------------")

while True :
    food=input("Select an item (q to quit) :")
    if food.lower()=="q" :
        break;
    elif manu.get(food) is not None :
        cart.append(food)

print("-------------YOUR ORDER-------------")
for food in cart :
    total +=manu.get(food)
    print(food,end=" ") 
    
print()
print(f"Total is : ${total:.2f}")
