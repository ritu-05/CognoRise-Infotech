import random

def roll_dice(num_sides, num_rolls):
    rolls = []
    for _ in range(num_rolls):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

def main():
    print("the Dice Rolling Simulator!")
    
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            if num_sides <= 0:
                raise ValueError("The number of sides must be a positive integer.")
            break
        except ValueError as e:
            print(e)
            continue

    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                raise ValueError("The number of rolls must be a positive integer.")
            break
        except ValueError as e:
            print(e)
            continue

    results = roll_dice(num_sides, num_rolls)
    print(f"\nResults of rolling a {num_sides}-sided dice {num_rolls} times:")
    print(results)

if __name__ == "__main__":
    main()
