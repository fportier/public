from Bicycle import Bicycle

class MountainBike(Bicycle):
    
    __seatHeight = None


    def __init__(self,  gear,  speed,  seatHeight):
        super().__init__( gear, speed)
        self.__seatHeight = seatHeight
    
    def setHeight(self, seatHeight):
        self.__seatHeight = seatHeight
 
    def __str__(self):
        return super().__str__() + "\nseat height is "\
                + str(self.__seatHeight)

    def __eq__(self,bk2):
        return super().__eq__(bk2) and self.__seatHeight == bk2.__seatHeight
