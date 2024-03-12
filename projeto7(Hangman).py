import random
import hangmanTools


print(hangmanTools.logo)
used = []

lives = 6
chosen = random.choice(hangmanTools.words).lower()

length = len(chosen)

word = ['_' for _ in range(length)]
stop = False
while not stop:
    j=0
    marcador = 0
    print(" ".join(word))
    print(hangmanTools.stages[lives])
    i = input("Guess a letter: ").lower()
    if i not in used:
        used.append(i)
        for aux in chosen:
            if aux == i:
                word[j] = i
                #print("Right")
                marcador += 1
                j += 1
            else:
                #print("Wrong")
                j += 1
        if marcador == 0:
            lives -= 1
            print(f"You guessed {i}, that's not in the word. You lose a life.")

        if lives <= 0:
            stop = True
            print("YOU LOSE")
            print(hangmanTools.stages[lives])
        elif "_" not in word:
            stop = True
            print("YOU WONN")
        print("Used Letters")
        print(" ".join(used))
        j=0
    else:
        print("You have already used this letter, try another one")


