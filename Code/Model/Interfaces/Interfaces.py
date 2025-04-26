from abc import ABC,abstractmethod

class IOrderDB(ABC):

    @abstractmethod 
    def select_items (self): 
        pass  
    @abstractmethod 
    def insert (self):
        pass
    @abstractmethod 
    def save (self):
        pass
    
class IUserDB(ABC):

    @abstractmethod 
    def select_items (self): 
        pass  
    @abstractmethod 
    def insert (self):
        pass
    @abstractmethod 
    def save (self):
        pass
class IItemDB(ABC):

    @abstractmethod 
    def select_items (self): 
        pass  
    @abstractmethod 
    def insert (self):
        pass
    @abstractmethod 
    def save (self):
        pass