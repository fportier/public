class Bicycle:

    __gear =  None 
    __speed = None

    def __init__(self,gear,speed):
        self.__gear = gear
        self.__speed = speed
    
    def applyBrake(self, decrement):
        self.__speed -= decrement
        
    def speedUp(self, increment): 
        self.__speed += increment
        

    def __str__(self):
        return "No of gears are " + str(self.__gear) + "\n" \
                + "speed of bicycle is " + str(self.__speed)
                
    def  __eq__(self,b2):
        return self.__gear == b2.__gear and self.__speed == b2.__speed
