import random
num = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
        if guess > num:
            print(f'Too High')
        elif guess < num:
            print(f'Too Low')
        else:
            print(f'You guessed the number correctly {num}')
            break
    except ValueError:
        print('You did not enter a number.')
