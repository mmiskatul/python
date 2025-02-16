#
rows=int(input("Enter the row size : "))
columns=int(input("Enter the columns size : "))
symbol=input("Enter a sybmol to use  : ")

for x in range(rows) :
    for y in range(columns):
        print(symbol,end=" ")
    print()