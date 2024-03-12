print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You want to go Left(L) or Right(R)? ")
if choice1 == "L":
    print("You Walk and find a island surrounded by a big lake.")
    choice2 = input("You want to swim(A) or wait a really convenient boat(B)?")
    if choice2 == "B":
        print("You swim to the island and found a cave with three dors")
        print("Which one do you open? The blue one?(A) The red one?(B) or The Yellow one?(C)")
        print("A goblin seated on a rock says: Pick the yellow one!")
        choice3 = input()
        if choice3 == "A":
            print("Congrats! You found a great room of pure air! END")
        elif choice3 == "B":
            print("LOL! Is locked! END")
        elif choice3 == "C":
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
            print("WOW! There's a lot of gold!")
            lastC = input("Do you want to share your trasure with the goblin?(Y/N)")
            if lastC == "N":
                print("Ok. You are a really bad person! END")
            else:
                print("He gaves you his eternal gratitude! END")
    else:                                
        print("A realy inconvenient aligator bites you. Game Over!")
else:
    print("You fall in a big big hole. Game Over!")