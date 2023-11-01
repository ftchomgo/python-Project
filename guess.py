import random
good_guess=10
number_try =1
while number_try <= 3:
    number_try = number_try+1
    try:
        choice = int(input("Please enter a number between 1 and 20: "))
        if choice not in range(1,21):
            print("Invalid entry")
        elif choice == good_guess:
            print("Good job you wont!!!") 
            break
        elif choice < good_guess:
            print("sorry your number is lower")
        elif choice > good_guess:
            print("sorry your number is bigger")
    except:
        print("something went wrong please")