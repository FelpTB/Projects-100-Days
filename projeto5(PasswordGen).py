import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total = nr_letters + nr_symbols + nr_numbers
password = []
rand = 0
rand2 = 0
let = nr_letters
sym = nr_symbols
num = nr_numbers
i = 0
while i < total:
    rand = random.randint(0,2)
    if rand == 0 and num > 0:
        rand2 = random.randint(0,9)
        password.append(random.choice(numbers))
        num -= 1
        i += 1
    elif rand == 1 and sym > 0:
        rand2 = random.randint(0,8)
        password.append(random.choice(symbols))
        sym -= 1
        i += 1
    elif rand == 2 and let > 0:
        rand2 = random.randint(0,51)
        password.append(random.choice(letters))
        let -= 1
        i += 1

word = ""
for i in password:
    word = word + i

print("Here is your password: " + word)

