import random

rNum = random.randint(1,101)

print("Welcome to the number guessing game, you'll be guessing a number between 1 - 100")
choice = input("Would you like to go the easy route or hard route: ").lower()
guess = 0
hardAttempt = 5
easyAttempt = 10
listTries = []
if choice == "easy":
    print(f"you chose hard so youll only have {easyAttempt} attempts: ")
    while guess != rNum:
        approx = int(input("Please guess a number: "))
        if approx in listTries :
            print("you have already guessed: " + str(approx))
            continue
        guess += 1
        listTries.append(approx)
        if (approx>rNum) : 
            easyAttempt = easyAttempt - 1
            print ("too high" ) 
            print(f"you have {easyAttempt} attempts to guess the num: ")
        elif (approx<rNum) : 
            easyAttempt = easyAttempt -1
            print("too low")
            print(f"you have {easyAttempt} attempts to guess the num: ")
        elif approx == rNum:
            print(f"you guessed the correct num which was {rNum}")
            break
        elif guess == 10: 
            print(f"10 attempts tried, the number is {rNum}: ")
for item in listTries:
    print(item)
if choice == "hard":
    print(f"you chose easy so youll only have {hardAttempt} attempts: ")
    while guess != rNum:
        approx = int(input("Please guess a number: "))
        if approx in listTries :
            print("you have already guessed: " + str(approx))
            continue
        guess += 1
        listTries.append(approx)
        if (approx>rNum) : 
            hardAttempt = hardAttempt - 1
            print ("too high" ) 
            print(f"you have {hardAttempt} attempts to guess the num: ")
        elif (approx<rNum) : 
            hardAttempt = hardAttempt -1
            print("too low")
            print(f"you have {hardAttempt} attempts to guess the num: ")
        elif approx == rNum:
            print(f"you guessed the correct num which was {rNum}")
            break
        elif guess == 10: 
            print(f"10 attempts tried, the number is {rNum}: ")