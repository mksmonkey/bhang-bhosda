import random

def hilo():
    if (guess < num):
        print("the number guessed is a little lower")
    if (guess > num):
        print("the number guessed is little higher")
        
print("WELCOME TO GUESS THE NUMBER")


while True:
    try:
        num = random.randint(0,20)
        guess = int(input("now guess the number i have chosen(its b/w 0-20) - "))
        if guess == num:
            print("you have guessed right in first guess")
        while (guess != num):
            hilo()
            guess = int(input("try again  - "))
            if guess == num:
                print("correct answer")
                break

    except ValueError:
        print("number likh le bhai!")
    break

input("Press Enter to leave")
    
