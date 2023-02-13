from Employee import  Employee

class HourlyEmployee(Employee):
     
    __wage = None
     
    def __init__(self,name,id,title,wage):
        super().__init__(name,id,title)
        self.__wage = wage
         
    def __str__(self):
        return super().__str__()+\
            "\nwage="+str(self.__wage)
            
    def setWage(self,wage):
        self.__wage = wage
        
    def getWage(self):
        return self.__wage
    
    def __eq__(self,other):
        return super().__eq__(other) and \
            self.__wage == other.__wage

