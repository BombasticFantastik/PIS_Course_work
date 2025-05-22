from abc import ABC,abstractmethod

class IOrderDB(ABC):
    @abstractmethod 
    def get_orders (self): 
        pass  
  
class IUserDB(ABC):

    @abstractmethod 
    def get_users (self): 
        pass
    
class IItemDB(ABC):

    @abstractmethod 
    def get_items (self): 
        pass  
