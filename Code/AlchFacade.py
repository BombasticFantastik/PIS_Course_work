from IFacade import IFacade

class AlchFasade(IFacade):
    def __init__(self,engine,base,session):
        self.engine=engine
        self.base=base
        self.session=session
    def select(self,object):
        self.session.add(object)
    def insert(self,):
        self.session.add(object)
    def update(self):
        