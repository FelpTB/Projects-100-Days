import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to the secret auction program.")
stop = False
bides = {}
greatest = 0
winner = ""
while not stop:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bides[name] = bid
    if bid >= greatest:
        greatest = bid
        winner = name
    other = input("Are there any other bidders? Type s/n.\n").lower()
    if other == "n":
        stop = True
    else:
        os.system('cls')
print(f"The winner is {winner} with a bid of ${greatest}")
    




