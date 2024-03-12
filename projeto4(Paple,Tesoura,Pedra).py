import random

choice = input("What do you choose? (Type 0 for Rock, 1 for Paper or 2 for Scissor)\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

mao = [rock,paper,scissors]

print(mao[int(choice)])
print("Computer chose")
print(mao[random.randint(0,2)])

