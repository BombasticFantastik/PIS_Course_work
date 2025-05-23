import sys
sys.path.insert(0, '/home/artemybombastic/Рабочий стол/Курсовая работа: проектирование информационных систем/Code/src')
from sqlalchemy import create_engine     
import datetime
from sqlalchemy.orm import sessionmaker
from Model.AlchFacade import AlchFacade
from Model.classes import Item
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

def test_get_users():
    assert type(Fasade.get_items()[0])==Item
    assert type(Fasade.get_items()[0].seller_id)==int
    assert type(Fasade.get_items()[0].name)==str


def create_item():
    Fasade.create_item(seller_id=999,name='Новый предмет',article=3333,price=1010,count=10)
    item=Fasade.get_items(article=3333)[0]
    assert type(item)==Item
    assert item.seller_id==999
    assert item.name=='Новый предмет'
    assert item.article==3333
    assert item.price==1010
    assert item.count==10
    Fasade.delete(item)
    