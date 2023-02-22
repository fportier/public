from Deck import Deck
from Card import Card

c = Card(12,"C")
print(c)

d = Deck("my Deck",[c])
d.addCard(Card(2,"D"))
d.addCard(Card(6,"S"))
d.addCard(Card(11,"H"))
d.addCard(Card(4,"S"))
d.addCard(Card(1,"D"))
print(d)

h1,h2 = d.deal(3,2)  # 2 players, each gets 3 cards
print(h1)
print(h2)
print(d)