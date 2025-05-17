import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit,QTableWidget,QTableWidgetItem
#from sqlalchemy import create_engine,Column,Integer,String,Float,Table,MetaData,insert,delete,update,text
class Communicate(QObject):
        signal = pyqtSignal(str)

class Admin_Cat(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,create_order_item_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.orders_fu=orders_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.create_order_item_fu=create_order_item_fu
        
        super().__init__()
        
        self.setWindowTitle("Warehouse")
        self.filtr_window = None

        self.setFixedSize(840,400)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(6)
        self.fill()

        #id
        self.id_select_label=QLabel('Введите Id')
        self.id_select = QLineEdit()

        #Добавить/Удалить/Найти
        self.button_filtr = QPushButton("Фильтр", self)
        self.button_orders = QPushButton("Ваши заказы", self)
        self.button_add=QPushButton('Добавить выбранный \n товар в заказ',self)
        self.button_filtr.setFixedSize(170,100) 
        self.button_orders.setFixedSize(170,100)  
        self.button_add.setFixedSize(170,100)     

        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.id_select_label)
        left_layout.addWidget(self.id_select)
        left_layout.addWidget(self.button_filtr)
        left_layout.addWidget(self.button_orders)
        left_layout.addWidget(self.button_add)


        
        

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)
        #кнопки
        self.button_filtr.clicked.connect(self.filtr)
        self.button_orders.clicked.connect(self.orders)
        self.button_add.clicked.connect(self.show_add_window)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
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
        
    def orders(self,data):
        #self.communication = Communicate()
        self.filtr_window=Selected_Order_window(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu)
        self.filtr_window.show()
        pass


    def add_to_order(self,message):
        selected_item=self.items_fu(id=self.id_select.text())
        selected_item=selected_item[0]
        self.create_order_item_fu(item_id=selected_item.id,order_id=2,count=int(message))#убрать
    def show_add_window(self):
        selected_item=self.items_fu(id=self.id_select)
        self.communication = Communicate()
        self.filtr_window=add_window(self.communication)
        self.communication.signal.connect(self.add_to_order)
        self.filtr_window.show()
        



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
        
        self.setWindowTitle("Ваши заказы")
        self.filtr_window = None

        self.setFixedSize(900,400)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(6)
        self.fill()

        #left
        self.id_select_label=QLabel('Введите Id')
        self.id_select = QLineEdit()
        self.go_to_order=QPushButton('Перейти к заказу \n с выбранным Id',self)
        self.id_select_label.setFixedSize(200,10)
        self.id_select.setFixedSize(200,50)
        self.go_to_order.setFixedSize(200,100)

        
        #left_layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.id_select_label)
        left_layout.addWidget(self.id_select)
        left_layout.addWidget(self.go_to_order)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)
        self.go_to_order.clicked.connect(self.go_to_ord_func)

        #main
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)
        #self.filttred_text=None



    def fill(self,orders=None):
        self.table.clear()
        self.table.setHorizontalHeaderLabels([
            'id',
            'seller_id',
            'admin_id',
            'created_in',
            'status',
            'total_price',
        ])
        if orders==None:
            orders=self.orders_fu()
        for i in orders:
            id=QTableWidgetItem(str(i.id))
            sell_id=QTableWidgetItem(str(i.seller_id))
            name=QTableWidgetItem(str(i.admin_id))
            art=QTableWidgetItem(str(i.created_in))
            price=QTableWidgetItem(str(i.status))
            cnt=QTableWidgetItem(str(i.total_price))
            costil=i.id
            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,sell_id)
            self.table.setItem(costil,2,name)
            self.table.setItem(costil,3,art)
            self.table.setItem(costil,4,price)
            self.table.setItem(costil,5,cnt)
    def go_to_ord_func(self):
        pass

class add_window(QWidget):
    
    def __init__(self,communication):
        super().__init__()
        self.com=communication
        #self.select_fu=
        

        #labels
        self.count_label=QLabel('Выберите количество товара')

        #inputs
        self.count_input=QLineEdit()

        #labels_layout
        labels_layout = QVBoxLayout()
        labels_layout.addWidget(self.count_label)
        labels_layout.addWidget(self.count_input)
        
        #inputs_labels
        input_layout=QVBoxLayout()
        #input_layout.addWidget(self.seller_input)

        #button
        self.add_button=QPushButton("Добавить")
        self.add_button.clicked.connect(self.chose_count)
        self.add_button.setFixedSize(150,75)
        input_layout.addWidget(self.add_button)

        

        main_layout = QHBoxLayout()
        main_layout.addLayout(labels_layout)
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)
    def chose_count(self):

        self.com.signal.emit(str(self.count_input.text()))


class Selected_Order_window(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        
        super().__init__()
        
        self.setWindowTitle("Детали вашего заказа")
        #self.filtr_window = None

        self.setFixedSize(560,400)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(350,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(3)
        self.fill()

        #left
        self.id_select_label=QLabel('Введите Id')
        self.id_select = QLineEdit()
        self.remove_detail=QPushButton('Удалить товар с \n с выбранным Id',self)
        self.remove_order=QPushButton('Отменить \n заказ',self)
        self.accept_order=QPushButton('Одобрить \n заказ',self)
        self.id_select_label.setFixedSize(200,10)
        self.id_select.setFixedSize(200,50)
        self.remove_detail.setFixedSize(200,100)
        self.remove_order.setFixedSize(200,100)
        self.accept_order.setFixedSize(200,100)

        
        #left_layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.id_select_label)
        left_layout.addWidget(self.id_select)
        left_layout.addWidget(self.remove_detail)
        left_layout.addWidget(self.remove_order)
        left_layout.addWidget(self.accept_order)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)
        #self.go_to_order.clicked.connect(self.go_to_ord_func)

        #main
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)
        #self.filttred_text=None



    def fill(self,order_items=None):
        self.table.clear()
        self.table.setHorizontalHeaderLabels([
            'item_id',
            'order_id',
            'count',
        ])
        if order_items==None:
            order_items=self.order_items_fu()
        print(order_items)
        for j,i in enumerate(order_items):
            item_id=QTableWidgetItem(str(i.item_id))
            sell_id=QTableWidgetItem(str(i.order_id))
            cnt=QTableWidgetItem(str(i.count))
            costil=1
            self.table.setItem(j,0,item_id)
            self.table.setItem(j,1,sell_id)
            self.table.setItem(j,2,cnt)
    def go_to_ord_func(self):
        pass