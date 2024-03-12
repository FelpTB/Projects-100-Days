import random
import time

## The deck is unlimited in size. V
cards = {
1:1,
11:11,
2:2,
3:3,
4:4,
5:5,
6:6,
7:7,
8:8,
9:9,
10:10,
"j":10,
"q":10,
"k":10,
}
deck = [11,2,3,4,5,6,7,8,9,10,"j","q","k"]
player = []
computer = []

def blackjack():
    stop = False
    
    player.append(random.choice(deck))
    player.append(random.choice(deck))
    computer.append(random.choice(deck))
    computerScore = cards[computer[0]]
    while not stop:
        playerScore = 0
        for aux in player:
            playerScore += cards[aux]
        if 11 in player and playerScore > 21:
            player.remove(11)
            player.append(1)
            playerScore -= 10
        print(f"your hand is {player}, your score is {playerScore}")
        print(f"Computer hand is {computer}")
        if 11 in player and playerScore > 21:
            player.remove(11)
            player.append(1)
            playerScore -= 10
        if playerScore > 21:
            print("You went over.")
            return
        next = input("Type 'y' to get another card and 'n' to pass: ").lower()
        if next == 'y' and playerScore < 21:
            player.append(random.choice(deck))
        else:
            stop = True
            i = 1
            while computerScore < 17 or playerScore > computerScore:
                computer.append(random.choice(deck))
                computerScore += cards[computer[i]]
                print(f"Dealer buys an {computer[i]} his score is now {computerScore}")
                if computerScore > 21:
                    print("dealer went over.")
                    print("Congrats, you win the game!")
                    return
                time.sleep(3)
                i += 1
            print(f"Dealer ends with {computerScore}, your score is {playerScore}.")
            if computerScore >= playerScore:
                print("The house Wins the game")
                return
            else:
                print("Congrats, you win the game!")
                return
play = True
while play:
    player = []
    computer = []
    blackjack()
    playAgain = input("Play Again? (y/n): ").lower()
    if playAgain == "n":
        play = False




## There are no jokers.V 
## The Jack/Queen/King all count as 10.V
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

