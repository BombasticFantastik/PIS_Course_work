from sqlalchemy import create_engine
#import psycopg2
import abc
from View.View import Admin_Cat,Filter_window,Admin_Orders_window,Selected_Order_window,add_window,Login_window,Seller_orders_window
import sys
from PyQt6.QtWidgets import QApplication
from Model.classes import Item,Order,Order_Item,User          
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from Model.AlchFacade import AlchFacade
import yaml
option_path='config.yaml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)

engine=create_engine(option['path'])
engine.connect()
Session=sessionmaker(bind=engine)
session=Session()
Fasade=AlchFacade(engine,session)
#item0=User(status='Поставщик',login='NewSeller',password='14',INN=222121311122,legal_entity='Александр Сурикович В.',address='Волочаевская 3 д. 3',registred_in='01-02-2024')
# item1=User(Status='Администратор',login='NewAdmin',password='14',INN=153456789112,legal_entity='Алексей Алексеевич В.',address='Волочаевская 160 д. 2',registred_in='02-02-2024')
# item1=Item(seller_id=1,name='Радиатор Spring',article=1112,price=2500,count=15)
#item2=Order(seller_id=1,admin_id=2,created_in='03-03-2024',status='Не отправленно',total_price=40000)
#Fasade.add(item0)
# Fasade.add(item1)
#Fasade.add(item2)


#print(Fasade.order_user_join()[0][0])

#Seller_orders_window

app = QApplication(sys.argv)
window = Login_window(Fasade.get_items,
                      Fasade.get_orders,
                      Fasade.get_users,
                      Fasade.get_order_items,
                      Fasade.add,
                      Fasade.delete,
                      Fasade.create_order_item,
                      Fasade.save,
                      Fasade.create_item,
                      Fasade.order_user_join,
                      Fasade.create_order,
                      Fasade.get_order_items_items_join
                      )
window.show()
sys.exit(app.exec())


