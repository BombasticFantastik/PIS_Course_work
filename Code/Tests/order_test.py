import sys
sys.path.insert(0, '/home/artemybombastic/Рабочий стол/Курсовая работа: проектирование информационных систем/Code/src')
from sqlalchemy import create_engine     
import datetime
from sqlalchemy.orm import sessionmaker
from Model.AlchFacade import AlchFacade
from Model.classes import Order
from sqlalchemy.orm import declarative_base

import yaml
option_path='config.yaml'
with open(option_path,'r') as file_option:
    option=yaml.safe_load(file_option)


engine=create_engine(option['path'])
engine.connect()
Session=sessionmaker(bind=engine)
session=Session()
Fasade=AlchFacade(engine,session)

def get_orders():
    item=Order(id=999,seller_id=999,admin_id=999,created_in='03-03-2020',status='Не отправленна',total_price=3000)
    Fasade.add(item)
    assert type(Fasade.get_orders(id=999)[0])==Order
    assert Fasade.get_orders(id=999)[0].seller_id==999
    assert Fasade.get_orders(id=999)[0].created_in==datetime.date(2020,3,3)
    Fasade.remove(item)


# def create_item():
#     Fasade.create_item(seller_id=999,name='Новый предмет',article=3333,price=1010,count=10)
#     item=Fasade.get_items(article=3333)[0]
#     assert type(item)==Item
#     assert item.seller_id==999
#     assert item.name=='Новый предмет'
#     assert item.article==3333
#     assert item.price==1010
#     assert item.count==10
#     Fasade.delete(item)
    