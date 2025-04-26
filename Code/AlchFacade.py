from Model.Interfaces.Interfaces import IFacade
from bd_classes import Item

class AlchFacade(IFacade):
    def __init__(self,engine,session):
        self.engine=engine
        self.session=session
    def select_items(self,seller_id=None,article=None,price=None,name=None):
        selected_users=self.session.query(Item)
        if seller_id:
            selected_users=selected_users.filter_by(seller_id=seller_id)
        if article:
            selected_users=selected_users.filter_by(article=article)
        if price:
            selected_users=selected_users.filter_by(price=price)
        if name:
            selected_users=selected_users.filter_by(name=name)
        return selected_users

    def insert(self,object):
        self.session.add(object)
    def delete(self,object):
        self.session.delete(object)
    def save(self):
        self.session.commit()
    def cancel(self):
        self.session.rollback()