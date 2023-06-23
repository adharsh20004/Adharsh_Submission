import random

def guess_the_number():
    name = input("Enter your name: ")
    print("Hello, " + name + "!")

    lower = int(input("Enter the lower limit : "))
    upper = int(input("Enter the upper limit : "))
    number = random.randint(lower, upper)

    total_points = 100

    while True:
        print("\nTotal points: " + str(total_points))

        guess = int(input("Guess the number: "))

        if guess == number:
            print("Congratulations, you guessed the number!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        total_points -= 5

        if total_points <= 0:
            print("Sorry, you ran out of points!")
            break

    print("\nThanks for playing, " + name + "!")
    print("Your final score is: " + str(total_points))


guess_the_number()