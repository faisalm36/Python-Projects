from art import logo
from art import vs
from gameData import data
import random
print(logo)

score = 0
game = True
accountB = random.choice(data)
while game :
    def generate(account):
        accountName = account['name']
        accountDesc = account['description']
        accountCountry = account['country']
        return f"{accountName}, a {accountDesc}, from {accountCountry}"

    accountA = accountB
    accountB = random.choice(data)

    def checkAnswer(guess, followerAccountA, followerAccountB):
        if followerAccountA > followerAccountB:
            return guess == 'a'
        else:
            return guess == 'b'


    if accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {generate(accountA)}.")
    print(vs)
    print(f"Against B: {generate(accountB)}.")

    # Asking the user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #checking if the user is correct and getting the follower account
    followerAccountA = accountA["follower_count"]
    followerAccountB = accountB["follower_count"]
    isCorrect = checkAnswer(guess, followerAccountA, followerAccountB)
    if isCorrect:
        score += 1
        print(f"You're right {score}")
    else:
        game = False
        print(f"Incorrect your score is {score}")
        quit()

