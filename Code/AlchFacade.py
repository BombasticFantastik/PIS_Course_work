from Interfaces import IItemDB,IOrderDB,IUserDB
from classes import Item,User,Order,Order_Item

class AlchFacade(IItemDB,IOrderDB,IUserDB):
    def __init__(self,engine,session):
        self.engine=engine
        self.session=session
    def get_users(self,id=None,status=None,login=None,password=None,INN=None,legal_entity=None,address=None):
        selected_users=self.session.query(User)
        if id:
            selected_users=selected_users.filter_by(id=id)
        if status:
            selected_users=selected_users.filter_by(article=status)
        if login:
            selected_users=selected_users.filter_by(login=login)
        if password:
            selected_users=selected_users.filter_by(password=password)
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
    
    def get_order_items(self,id=None,item_id=None,order_id=None,cnt=None):
        selected_order_items=self.session.query(Order_Item)
        if id:
            selected_order_items=selected_order_items.filter_by(id=id)
        if item_id:
            selected_order_items=selected_order_items.filter_by(item_id=item_id)
        if order_id:
            selected_order_items=selected_order_items.filter_by(order_id=order_id)
        if cnt:
            selected_order_items=selected_order_items.filter_by(count=cnt)
        return selected_order_items

    def add(self,object):
        self.session.add(object)
        self.save()
    def delete(self,object):
        self.session.delete(object)
        self.save()
    def save(self):

        self.session.commit()

    def create_order_item(self,item_id,order_id,count):
        selected_item=self.get_items(id=item_id)[0]
        if selected_item.count<count:
            return False
        else:
            selected_item.count-=count
            self.add(Order_Item(item_id=item_id,order_id=order_id,count=count))
            return True


    def create_item(self,seller_id,name,article,price,count):
        self.add(Item(seller_id=seller_id,name=name,article=article,price=price,count=count))

    # def cancel_changes(self):
    #     self.session.rollback()