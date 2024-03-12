print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
div = int(input("How many people to split the bill? "))
payment = round((total + (total * percentage))/div,2)
print(f"Each person should pay: ${payment}")