from Interfaces import IItemDB,IOrderDB,IUserDB
from classes import Item,User,Order

class AlchFacade(IItemDB,IOrderDB,IUserDB):
    def __init__(self,engine,session):
        self.engine=engine
        self.session=session
    def get_users(self,id=None,status=None,INN=None,legal_entity=None,address=None):
        selected_users=self.session.query(User)
        if id:
            selected_users=selected_users.filter_by(id=id)
        if status:
            selected_users=selected_users.filter_by(article=status)
        if INN:
            selected_users=selected_users.filter_by(INN=INN)
        if legal_entity:
            selected_users=selected_users.filter_by(legal_entity=legal_entity)
        if address:
            selected_users=selected_users.filter_by(address=address)
        return selected_users
    
    def get_items(self,id=None,seller_id=None,article=None,price=None,name=None):
        selected_items=self.session.query(Item)
        if id:
            selected_items=selected_items.filter_by(id=id)
        if seller_id:
            selected_items=selected_items.filter_by(seller_id=seller_id)
        if article:
            selected_items=selected_items.filter_by(article=article)
        if price:
            selected_items=selected_items.filter_by(price=price)
        if name:
            selected_items=selected_items.filter_by(name=name)
        
        return selected_items
    
    def get_orders(self,id=None,seller_id=None,admin_id=None,created_in=None, status=None,total_price=None):
        selected_orders=self.session.query(Order)
        if id:
            selected_orders=selected_orders.filter_by(id=id)
        if seller_id:
            selected_orders=selected_orders.filter_by(seller_id=seller_id)
        if admin_id:
            selected_orders=selected_orders.filter_by(admin_id=admin_id)
        if created_in:
            selected_orders=selected_orders.filter_by(created_in=created_in)
        if status:
            selected_orders=selected_orders.filter_by(status=status)
        if created_in:
            selected_orders=selected_orders.filter_by(created_in=created_in)
        return selected_orders
    

    def add(self,object):
        self.session.add(object)
    def delete(self,object):
        self.session.delete(object)
    def save(self):
        self.session.commit()
    def cancel_changes(self):
        self.session.rollback()