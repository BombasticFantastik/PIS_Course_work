import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit,QTableWidget,QTableWidgetItem
#from sqlalchemy import create_engine,Column,Integer,String,Float,Table,MetaData,insert,delete,update,text
class Communicate(QObject):
        signal = pyqtSignal(str)

class Admin_Cat(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,add_fu,del_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        
        super().__init__()
        
        self.setWindowTitle("Warehouse")
        self.filtr_window = None

        self.setFixedSize(1280,500)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(6)
        self.fill()

        

        #Добавить/Удалить/Найти
        self.button_Add = QPushButton("Фильтр", self)
        self.button_Remove = QPushButton("Удалить", self)
        self.button_Select=QPushButton('Выбрать',self)

        #задаём размеры




        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.button_Add)
        

        #правый
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.button_Remove)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        table_layout.addWidget(self.button_Select)

        #кнопки
        self.button_Add.clicked.connect(self.filtr)
        self.button_Remove.clicked.connect(self.remove)
        self.button_Select.clicked.connect(self.select)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)






        self.filttred_text=None



    def fill(self,items=None):
        self.table.clear()
        self.table.setHorizontalHeaderLabels([
            'id',
            'seller_id',
            'name',
            'article',
            'price',
            'count',
        ])
        if items==None:
            items=self.items_fu()
        for i in items:

            id=QTableWidgetItem(str(i.id))
            sell_id=QTableWidgetItem(str(i.seller_id))
            name=QTableWidgetItem(str(i.name))
            art=QTableWidgetItem(str(i.article))
            price=QTableWidgetItem(str(i.price))
            cnt=QTableWidgetItem(str(i.count))

            costil=i.id

            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,sell_id)
            self.table.setItem(costil,2,name)
            self.table.setItem(costil,3,art)
            self.table.setItem(costil,4,price)
            self.table.setItem(costil,5,cnt)

                

    

    def filtr(self):
        self.communication = Communicate()
        
        self.filtr_window=Filter_window(select_fu=self.items_fu,communication=self.communication)
        self.communication.signal.connect(self.update_label)
        self.filtr_window.show()
        

    def update_label(self, message):
        message=message.split('%')
        print(message)
        self.fill(self.items_fu(message[0],None,message[3],message[2],message[1]))
        #self,id=None,seller_id=None,article=None,price=None,name=None
        
    def remove(self):
        pass
    def select(self):
        print(self.select_fu()[0])
        
    def show_table(self,data):
        pass


class Filter_window(QWidget):
    
    def __init__(self,select_fu,communication):
        super().__init__()
        self.select_fu=select_fu
        self.con=communication
        
        
        
    
        #labels
        self.seller_label=QLabel('id')
        self.name_label=QLabel('name')
        self.price_label=QLabel('price')
        self.art_label=QLabel('art')

        #inputs
        self.seller_input=QLineEdit()
        self.name_input=QLineEdit()
        self.price_input=QLineEdit()
        self.art_input=QLineEdit()

        #labels_layout
        labels_layout = QVBoxLayout()
        labels_layout.addWidget(self.seller_label)
        labels_layout.addWidget(self.name_label)
        labels_layout.addWidget(self.price_label)
        labels_layout.addWidget(self.art_label)

        #inputs_labels
        input_layout=QVBoxLayout()
        input_layout.addWidget(self.seller_input)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.price_input)
        input_layout.addWidget(self.art_input)
        #button
        self.filtr_button=QPushButton("Отфильтровать")
        self.filtr_button.clicked.connect(self.filtr)
        input_layout.addWidget(self.filtr_button)

        

        main_layout = QHBoxLayout()
        main_layout.addLayout(labels_layout)
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)
    def filtr(self):

        self.con.signal.emit(f'{self.seller_input.text()}%{self.name_input.text()}%{self.price_input.text()}%{self.art_input.text()}')

class Admin_Orders_window(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,add_fu,del_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        
        super().__init__()
        
        self.setWindowTitle("Warehouse")
        self.filtr_window = None

        self.setFixedSize(1280,500)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(6)
        self.fill()

        

        #Добавить/Удалить/Найти
        self.button_Add = QPushButton("Фильтр", self)
        self.button_Remove = QPushButton("Удалить", self)
        self.button_Select=QPushButton('Выбрать',self)

        #задаём размеры




        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.button_Add)
        

        #правый
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.button_Remove)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        table_layout.addWidget(self.button_Select)

        #кнопки
        self.button_Add.clicked.connect(self.filtr)
        self.button_Remove.clicked.connect(self.remove)
        self.button_Select.clicked.connect(self.select)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)






        self.filttred_text=None



    def fill(self,items=None):
        self.table.clear()
        self.table.setHorizontalHeaderLabels([
            'id',
            'seller_id',
            'name',
            'article',
            'price',
            'count',
        ])
        if items==None:
            items=self.items_fu()
        for i in items:

            id=QTableWidgetItem(str(i.id))
            sell_id=QTableWidgetItem(str(i.seller_id))
            name=QTableWidgetItem(str(i.name))
            art=QTableWidgetItem(str(i.article))
            price=QTableWidgetItem(str(i.price))
            cnt=QTableWidgetItem(str(i.count))

            costil=i.id

            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,sell_id)
            self.table.setItem(costil,2,name)
            self.table.setItem(costil,3,art)
            self.table.setItem(costil,4,price)
            self.table.setItem(costil,5,cnt)

                

    

    def filtr(self):
        self.communication = Communicate()
        
        self.filtr_window=Filter_window(select_fu=self.items_fu,communication=self.communication)
        self.communication.signal.connect(self.update_label)
        self.filtr_window.show()
        

    def update_label(self, message):
        message=message.split('%')
        print(message)
        self.fill(self.items_fu(message[0],None,message[3],message[2],message[1]))
        #self,id=None,seller_id=None,article=None,price=None,name=None
        
    def remove(self):
        pass
    def select(self):
        print(self.select_fu()[0])
        
    def show_table(self,data):
        pass

        