class Card:
    __suit = None
    __value = None
    
    def __init__(self,value,suit):
        self.__suit = suit
        self.__value = value
        
    def getSuit(self):
        return self.__suit
    
    def getValue(self):
        return self.__value
    
    def setSuit(self,suit):
        self.__suit = suit
        
    def setValue(self,value):
        self.__value = value
    
    def __eq__(self,c2):
        return self.equalValue(c2) and self.equalSuit(c2)
    
    def __str__(self):
        return "({:d},{:s})".format(self.__value,self.__suit)
    
    def equalValue(self,c2):
        return self.__value == c2.__value
    
    def equalSuit(self,c2):
        self.__suit == c2.__suit