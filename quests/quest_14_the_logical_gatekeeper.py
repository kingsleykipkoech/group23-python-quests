age = int(input("Enter your age: "))  # get age from user
gold = int(input("Enter the amount of gold you have: "))  # get gold amount

if age >= 18 and gold >= 20:  # both must be true to enter
    print("You may enter the club!")
else:
    print("You cannot enter the club.")
