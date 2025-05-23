import sys
sys.path.insert(0, '/home/artemybombastic/Рабочий стол/Курсовая работа: проектирование информационных систем/Code/src')
from sqlalchemy import create_engine     
import datetime
from sqlalchemy.orm import sessionmaker
from Model.AlchFacade import AlchFacade
from Model.classes import Order,User
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
    
def test_get_orders():
    item=Order(id=999,seller_id=999,admin_id=999,created_in='03-03-2020',status='Не отправленна',total_price=3000)
    
    Fasade.add(item)
    assert type(Fasade.get_orders(id=999)[0])==Order
    assert Fasade.get_orders(id=999)[0].seller_id==999
    assert Fasade.get_orders(id=999)[0].created_in==datetime.date(2020,3,3)
    assert len(list(Fasade.get_orders(id=-12301)))==0
    Fasade.delete(item)
    
def test_create_create_order():
    Fasade.create_order(seller_id=999,admin_id=999,created_in='03-03-2020',status='Не отправленна',total_price=3000)
    item=Fasade.get_orders(seller_id=999,admin_id=999)[0]
    assert type(item)==Order
    assert item.status=='Не отправленна'
    Fasade.delete(item)

def test_order_user_join():
    assert type(Fasade.order_user_join()[0][1])==User
    assert type(Fasade.order_user_join()[0][0])==Order
    
