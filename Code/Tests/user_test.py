import sys
sys.path.insert(0, '/home/artemybombastic/Рабочий стол/Курсовая работа: проектирование информационных систем/Code/src')
from sqlalchemy import create_engine     
import datetime
from sqlalchemy.orm import sessionmaker
from Model.AlchFacade import AlchFacade
from Model.classes import User
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
    assert type(Fasade.get_users()[0])==User
    assert type(Fasade.get_users()[0].id)==int
    assert Fasade.get_users()[0].status in ['Администратор','Поставщик']
    assert type(Fasade.get_users()[0].registred_in)==datetime.date
    assert type(Fasade.get_users()[0].login)==str