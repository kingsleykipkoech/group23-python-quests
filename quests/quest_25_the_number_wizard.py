secret_number = 42
guess = 0 

while guess != secret_number:
    
    guess = int(input("Guess the secret number: "))
    
    if guess < secret_number:
        print("Too low Try again.")
        
    elif guess > secret_number:
        print("Too high Try again.")


print("Correct You cracked the code.")