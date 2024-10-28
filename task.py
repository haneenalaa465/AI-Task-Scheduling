class Task:
    def __init__(self,ID, description, duration, deadline, dependencies):
        self.__ID = ID
        self.__description = description
        self.__duration = duration
        self._deadline = deadline
        self._dependencies = dependencies
    
    def setID(self, ID):
        self.__ID = ID
    
    def getID(self):
        return self.__ID

    def setDescription(self, description):
        self.__description = description
    
    def getDescription(self):
        return self.__description
    
    def setDuration(self, duration):
        self.__duration = duration
    
    def getDuration(self):
        return self.__duration
    
    def setDeadline(self, deadline):
        self._deadline = deadline
    
    def getDeadline(self):
        return self._deadline
    
    def setDependies(self, dependencies):
        self._dependencies = dependencies
    
    def getDependies(self):
        return self.__dependencies

    
    