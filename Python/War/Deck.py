import random
from Card import Card

class Deck:
    __cards = None
    __cols = 5
    __title = None

    def __init__(self,title,L=[]):
        self.__cards = L[:]
        self.__title = title
        
    def addCard(self,c):
        self.__cards.append(c)
        
    def clearDeck(self):
        self.__cards=[]
        
    def shuffle(self):
        random.shuffle(self.__cards)
        
    def getFirst(self):
        return self.__cards.pop(0)
    
    def setCols(self,cols):
        Deck.__cols = cols
        
    def getCols(self):
        return self.__cols
    
    def size(self):
        return len(self.__cards)
    
    def getLast(self):
        return self.__cards.pop()
    
    def deal(self,num,players=1):
        L = []
        for t in range(players):
            L.append([])
        for i in range(num):
            for t in range(players):
                L[t].append(self.getFirst())
        return [Deck("Hand"+str(k+1),L[k]) for k in range(players)]
    
    def __str__(self):
        count = 1
        out = self.__title+"\n"
        for c in self.__cards:
            out += "{:10s}".format(str(c))
            if count % Deck.__cols ==0:
                out += "\n"
            count+=1
        return out
    