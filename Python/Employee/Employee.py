class Employee:
    
    __name = None
    __id = None
    __title = None
    
    def __init__(self,name,id,title):
        self.__name = name
        self.__id = id
        self.__title = title
    
    def __str__(self):
        return "Name="+self.__name+\
                "\nid= "+str(self.__id)\
                +"\ntitle= "+self.__title
    
    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def getTitle(self):
        return self.__title
    
    def setName(self,name):
        self.__name = name

    def setId(self,id):
        self.__id =  id

    def setTitle(self,title):
        self.__title = title
        
    def __eq__(self,other):
        return self.__name == other.__name and \
            self.__id == other.__id and \
            self.__title == other.__title