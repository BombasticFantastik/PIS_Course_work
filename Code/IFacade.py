from abc import ABC,abstractmethod

class IFacade(ABC):
    @abstractmethod 
    def __init__(self): 
        pass  
    @abstractmethod 
    def select (self): 
        pass  
    @abstractmethod 
    def insert (self):
        pass
    @abstractmethod 
    def update (self):
        pass
    @abstractmethod 
    def save (self):
        pass
    