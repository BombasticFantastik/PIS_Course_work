from sqlalchemy import create_engine
import psycopg2
import abc
from View import Admin_Cat,Filter_window,Admin_Orders_window,Selected_Order_window
import sys
from PyQt6.QtWidgets import QApplication
from classes import Item,Order,Order_Item
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from AlchFacade import AlchFacade
import yaml
option_path='config.yaml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)
engine=create_engine(option['path'])
engine.connect()
Session=sessionmaker(bind=engine)
session=Session()
Fasade=AlchFacade(engine,session)
#item0=Order_Item(item_id=1,order_id=1,count=15)
# item1=Order(id=1,seller_id=3,name="Камера для шины Mersedes Banse",article=3333,price=1500,count=20)
# item2=Order(seller_id=1,name="Покрышка Mersedes Banse",article=1235,price=2500,count=11)
#Fasade.add(item0)
# Fasade.add(item1)
# Fasade.add(item2)


# app = QApplication(sys.argv)
# window = Admin_Cat(Fasade.get_items,Fasade.get_orders,Fasade.get_users,Fasade.add,Fasade.delete)
# window.show()
# sys.exit(app.exec())

app = QApplication(sys.argv)
window = Selected_Order_window(Fasade.get_items,Fasade.get_orders,Fasade.get_users,Fasade.get_order_items,Fasade.add,Fasade.delete)
window.show()
sys.exit(app.exec())

# app = QApplication(sys.argv)
# window = Admin_Orders_window(Fasade.get_items,Fasade.get_orders,Fasade.get_users,Fasade.add,Fasade.delete)
# window.show()
# sys.exit(app.exec())
