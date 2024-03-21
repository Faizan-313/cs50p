import random


def main():
    level = get_level()
    score = simulate_game(level)
    print("score = ",score)

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l in [1,2,3]:
                break
        except:
            pass
    return l



def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def three_tries(x,y):
    count = 0
    while count < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                count += 1
                print("EEE")
        except:
            count += 1
            print("EEE")
    print(f"{x} = {y} = {x + y}")
    return False

def simulate_game(level):
    count = 0
    score = 0
    while count < 10:
        x ,y = generate_integer(level)
        response = three_tries(x,y)
        if response == True:
            score += 1
        count += 1
    return score


if __name__ == "__main__":
    main()
