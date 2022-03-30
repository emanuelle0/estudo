import random
cardValues = { 
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
    }

def countPoint(cardsOne, cardsTwo):
    if cardValues[cardsOne] > cardValues[cardsTwo]:
        return 1
    elif cardValues[cardsTwo] > cardValues[cardsOne]:
        return 0
    else:
        return 2

def countPointers(listPoints):
    pointsOne = 0
    pointsTwo = 0
    for i in listPoints:
        if i ==  1:
            pointsOne += 1
        elif i == 0:
            pointsTwo += 1
        else:
            pointsTwo += 1
            pointsOne += 1
    if pointsOne > pointsTwo:
        return f'Player One Wins {pointsOne} x {pointsTwo}'
    elif pointsTwo > pointsOne:
        return f'Player Two Wins {pointsTwo} x {pointsOne}'
    else:
        return 'Its a draw.'

def setCardsAndDelete(indexes):
    newList = []
    for i in indexes:
        newList += [cards[i]]

    return newList


cards =  list(cardValues.keys() ) * 4
playerOne = random.sample(range(52), k=10)
playerTwo = random.sample(range(42), k=10)

playerOneCards = setCardsAndDelete(playerOne)
playerTwoCards = setCardsAndDelete(playerTwo)

whoWins = list(map(countPoint, playerOneCards, playerTwoCards))
print(whoWins)
print(countPointers(whoWins))



    