# def  happy_birthday(name) :
#     print(f"Happy Birthday to {name}")
#     print("You are old ")
#     print(f"Happy Birthday to {name}")
#     print()
    
# happy_birthday("Miskatul");

# def display_invoice(user_name,amout,due_date):
#     print(f"Hello {user_name} ")
#     print(f"Your Bill of  $ {amout:.2f} is due : {due_date} ")
    
    
# display_invoice("Miskatul",69.99,"01/01/2025")
    
def create_name(first,last):
    first=first.capitalize();
    last=last.capitalize();
    return first+" "+last

full_name=create_name("Mistkaul","Masabi")
print(full_name)
