import random  # Importing the random library to simulate randomness

number = 6

def roll_dice():
    print("Rolling the dice...")
    dice1 = random.randint(1,number)
    dice2 = random.randint(1,number)
    total = dice1 + dice2
    print(f"You rolled a {dice1} and a {dice2} and a total of {total}")

def main():
    dice1 = 10
    print("dice1 in main() starts as : " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("dice1 in main() ends as : " + str(dice1))


if __name__ == '__main__':
    main()
