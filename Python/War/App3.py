from Deck import Deck
from Card import Card

def move(discard,hand):
    
    while discard.size() > 0:
        hand.addCard(discard.getFirst())

def createDeck():
    cards = [Card(v,s) for v in range(1,14) for s in "HCDS" ]
    deck = Deck("Deck",cards)
    deck.setCols(4)
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
        discard1.addCard(c1)
        discard2.addCard(c2)

def playGame(hand1,hand2,nplay):
    discard1 = Deck("Discard1")
    discard2 = Deck("Discard2")
    count = 0
    while hand1.size() > 0 and hand2.size() > 0:
        count += 1
        if count > 100:
             return discard1, discard2 
        c1 = hand1.getFirst()
        c2 = hand2.getFirst()
        compareCards(c1,c2,discard1,discard2)
        if hand1.size() == 0:
            move(discard1,hand1) 
        if hand2.size() == 0:
            move(discard2,hand2)       
    return discard1, discard2

def results(discard1,discard2):
    if discard1.size() > discard2.size():
        print("player 1 wins")
    elif discard1.size() < discard2.size():
        print("player 2 wins")
    else:
        print("its a tie")

def main():
    numCardPlay = 5
    deck = createDeck()
    hand1,hand2 = deck.deal(numCardPlay,2)
    print(hand1)
    print(hand2)
    discard1,discard2 = playGame(hand1,hand2,numCardPlay)
    print(discard1)
    print(discard2)
    results(discard1,discard2)

main()