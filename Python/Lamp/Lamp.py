class Lamp:
    __isOn = None
       
    def __init__(self,*args):
        if len(args)==0:
            self.__isOn = False
        else:
            self.__isOn= args[0]
            
    def turnOn(self):
        self.__isOn = True
    
    def turnOff(self):
        self.__isOn = False   
        
        
    def flip(self):
        self.__isOn = not self.__isOn
    
    def isOn(self):
        return self.__isOn
        
    def setLamp(self,isOn):
        self.__isOn = isOn
          
    def __str__(self):
        if self.__isOn:
            out = "{:3s}".format("ON")
        else:
            out = "{:3s}".format("OFF")
        return out
    
    def equals(self,other):
        return self.__isOn == other.__ison
