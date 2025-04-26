from sqlalchemy import create_engine,Column,Integer,String,Float,Date
import psycopg2
import abc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from Model.Interfaces.AlchFacade import AlchFacade
from bd_classes import Item

engine=create_engine('postgresql+psycopg2://postgres:12345@localhost/pis_base')
engine.connect()

Session=sessionmaker(bind=engine)
sesion=Session()

fac=AlchFacade(engine=engine,session=sesion)