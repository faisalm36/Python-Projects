import random
def dealCards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
for x in range(2):
    newCards = dealCards()
    user.append(dealCards())
    comp.append(dealCards())
def calcScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum (cards) > 21:
        cards.remove(11) 
        cards.append(1)
if comp