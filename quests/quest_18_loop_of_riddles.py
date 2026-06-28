def loop_of_riddles():
    secret_number = 7
    guess = int(input("Guess the secret number: "))
    while guess != secret_number:
        print("Wrong! Try again.")
        guess = int(input("Guess the secret number: "))
    print("You got it! The number was 7.")

loop_of_riddles()