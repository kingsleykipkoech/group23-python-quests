secret_code = 42
attempts = 3

for i in range(attempts):
    guess = int(input("Guess the secret code: "))
    if guess == secret_code:
        print("Your guess was correct")
        break
    else:
        print("Wrong guess. Try again.")
else:
    print("Out of attempts the secret  code  was 42.")
