import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number (1 to {x}): "))
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")    
    print(f"yes, it is {guess}")    


def computer_guess(x):
    count = 0

    low=1
    high=x
    feedback = ''
    while feedback != 'c':

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too low(l), high(h) or correct(c)?").lower()
        count = count + 1
        print(f"you said {feedback}")
        if feedback == 'h':
            if (guess - low) > 0:
                high = guess - 1
            else: 
                feedback = 'c'
                print (f"must be {guess}")

        elif feedback == 'l':
            if (high - guess) > 0:
                low = guess + 1
            else: 
                feedback = 'c'
                print (f"must be {guess}")    
        if high == low:
            feedback = 'c' 
            guess = high       
    print(f"It was {guess}, used {count} attempts.")            




#guess(10)
computer_guess(1000)



