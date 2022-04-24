# ----------------------------[main]--------------------------
print('''
        list
---------------------
p - pepsi       - 10/-
c - coke        - 10/-
s - sprite      - 15/-
m - miranda     - 20/-
---------------------
''')

# Variable
requiredAmountpepsi = 10
requiredAmountcoke = 10
requiredAmountsprite = 15
requiredAmountmiranda = 20

requiredItem = input("which drink do you want? ")
inputAmount = int(input("please enter the amount = "))

if requiredItem == 'p':

    if inputAmount < requiredAmountpepsi:
        print("insufficient amount")

    elif inputAmount > requiredAmountpepsi:
        balance = inputAmount - requiredAmountpepsi
        print(f"here's your balance amount = {balance}  ")
        print("here's your drink")

    else:
        print("here's your drink")

elif requiredItem == 'c':

    if inputAmount < requiredAmountcoke:
        print("insufficient amount")

    elif inputAmount > requiredAmountcoke:
        balance = inputAmount - requiredAmountcoke
        print(f"here's your balance amount = {balance} ")
        print("here's your drink")

    else:
        print("here's your drink")

elif requiredItem == 's':

    if inputAmount < requiredAmountsprite:
        print("insufficient balance")
        
    elif inputAmount > requiredAmountsprite:
        balance = inputAmount - requiredAmountsprite
        print(f"here's your balance amount = {balance} ")
        print("here's your drink")

    else:
        print("here's your drink")

elif requiredItem == 'm':

    if inputAmount < requiredAmountmiranda:
        print("insufficient balance")

    elif inputAmount > requiredAmountmiranda:
        balance = inputAmount - requiredAmountmiranda
        print(f"here's your balance amount = {balance}  ")
        print("here's your drink")

    else:
        print("here's your drink")

else:
    print("error")