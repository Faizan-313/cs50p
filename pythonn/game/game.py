import random

#promt user for upper value
while True:
    try:
        l = int(input("Level: "))
        if l > 0:
            break

    #if the user types other than int, prompt user again
    except ValueError:
        continue

#generate a random integer between 1 and the users upper limit
g = random.randint(1,l)

#promt user for guess number
while True:
    try:
        guess = int(input("Guess: "))
        if guess > l:
            continue
        elif guess > 0:
             #print message according to users guess
            if guess < g:
                print("Too small!")
            elif guess > g:
                print("Too large!")
            else:
                 print("Just right!")
                 exit()
    except ValueError:
        continue




