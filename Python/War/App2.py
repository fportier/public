from Deck import Deck
from Card import Card

def createDeck():
    cards = [Card(1+v%5,s) for v in range(1,14) for s in "HCDS" ]
    deck = Deck("Deck",cards)
    deck.setCols(10)
    deck.shuffle()
    return deck

def compareCards(c1,c2,discard1,discard2):
    if c1.getValue() > c2.getValue():
        discard1.addCard(c1)
        discard1.addCard(c2)
    elif c1.getValue() < c2.getValue():
        discard2.addCard(c1)
        discard2.addCard(c2) 
    else:
        return "equal"
    
def awardPrize(prize,discard,a,b):
    for x in prize:
        discard.addCard(x)
    discard.addCard(a)
    discard.addCard(b)

def ranOutOfCards(prize,discard1,discard2):
    count = 1
    for x in prize:
        if count % 2 == 0:
            discard1.addCard(x)
        else:
            discard2.addCard(x)
            count += 1 
    
def goToWar(c1,c2,discard1,discard2,hand1,hand2):
    print("its war!!!")
    done = False
    print(c1,c2)
    prize = []
    while not done and hand1.size() > 1 and hand2.size() > 1:     
        d1 = hand1.getFirst()
        d2 = hand2.getFirst()
        prize = [c1,c2,d1,d2]
        c1 = hand1.getFirst()
        c2 = hand2.getFirst()
        if c1.getValue() == c2.getValue():
            prize.append(c1)
            prize.append(c2)
        else:
            done = True
            if c1.getValue() > c2.getValue():
                awardPrize(prize,discard1,c1,c2)
            else:
                awardPrize(prize,discard2,c2,c1)
            break
    if done:
        return
    else:
        ranOutOfCards(prize,discard1,discard2)
        
         
                

def playGame(hand1,hand2,nplay):
    discard1 = Deck("Discard1")
    discard2 = Deck("Discard2")
    
    while hand1.size() > 0 and hand2.size() > 0:
        c1 = hand1.getFirst()
        c2 = hand2.getFirst()
        result  = compareCards(c1,c2,discard1,discard2)
        if result == "equal":
            goToWar(c1,c2,discard1,discard2, hand1,hand2)
    return discard1, discard2

def results(discard1,discard2):
    if discard1.size() > discard2.size():
        print("player 1 wins")
    elif discard1.size() < discard2.size():
        print("player 2 wins")
    else:
        print("its a tie")

def main():
    numCardPlay = 10
    deck = createDeck()
    hand1,hand2 = deck.deal(numCardPlay,2)
    print(hand1)
    print(hand2)
    discard1,discard2 = playGame(hand1,hand2,numCardPlay)
    print(discard1)
    print(discard2)
    results(discard1,discard2)

main()