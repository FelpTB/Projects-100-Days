
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Add
def add(n1, n2):
    return n1+n2

#Sub
def sub(n1,n2):
    return n1-n2

#mult
def mult(n1,n2):
    return n1 * n2

#div
def div(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "/":div,
    "*":mult
}

def calculator():
    n1 =float(input("What's the first number?: "))
    n2 =float(input("What's the second number?: "))
    for op in operations:
        print(op)
    opSym = input("Pick an operation from the line above: ")

    answer = operations[opSym](n1,n2)
    print(f"{n1} {opSym} {n2} = {answer}")
    stop = False
    next = input("Do you want to continue? (y/n) ").lower()
    if next == "n":
        stop = True

    while not stop:   
        for op in operations:
            print(op)
        opSym = input("Pick another operation from the line above: ")
        n1 = answer
        answer = operations[opSym](n1,n2)
        n2 =float(input("What's the next number?: "))
        print(f"{n1} {opSym} {n2} = {answer}")
        next = input("Do you want to continue? (y/n) ").lower()
        if next == "n":
            stop = True
            newCalc = input("Do you want to do another operation? (y/n) ").lower()
            if newCalc == "s":
                calculator()

            
print(logo)
print("Welcome to the calculator")
calculator()



