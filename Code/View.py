import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit,QTableWidget,QTableWidgetItem
#from sqlalchemy import create_engine,Column,Integer,String,Float,Table,MetaData,insert,delete,update,text
class Communicate(QObject):
        signal = pyqtSignal(str)


class Login_window(QWidget):
    
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,create_order_item_fu):
        super().__init__()

        self.setWindowTitle("Окно входа")
        
        #закрепляем 
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.orders_fu=orders_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.create_order_item_fu=create_order_item_fu
        

        
        self.seller_label=QLabel('Логин')
        self.name_label=QLabel('Пароль')

        #inputs
        self.login_input=QLineEdit()
        self.password_input=QLineEdit()

        #labels_layout
        labels_layout = QVBoxLayout()
        labels_layout.addWidget(self.seller_label)
        labels_layout.addWidget(self.name_label)

        #inputs_labels
        input_layout=QVBoxLayout()
        input_layout.addWidget(self.login_input)
        input_layout.addWidget(self.password_input)

        #button
        self.enter_button=QPushButton("Войти")
        self.enter_button.setFixedSize(120,90)
        self.enter_button.clicked.connect(self.log_in)
        

        main_layout = QHBoxLayout()
        main_layout.addLayout(labels_layout)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.enter_button)
        self.setLayout(main_layout)
    def log_in(self):
        selected_user=self.users_fu(login=self.login_input.text(),password_hash=self.password_input.text())
        
        if selected_user[0].login==self.login_input.text() and selected_user[0].password_hash==self.password_input.text():
            #Админ
            if selected_user[0].Status=='Aдминистратор':#??????????? как я мог себе это позволить ?
                self.admin_cat_window=Admin_Cat(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu,self.create_order_item_fu)
                self.admin_cat_window.show()
                self.close()
            #Поставщик
            else:
                pass
        else:
            pass

        


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
        self.setWindowTitle("Главное окно администратора")
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
        #конект
        self.button_filtr.clicked.connect(self.show_filtr_window)
        self.button_orders.clicked.connect(self.show_orders_window)
        self.button_add.clicked.connect(self.show_add_window)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)

    #заполнение данных в таблицу
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

    #окно фильтра
    def show_filtr_window(self):

        self.communication = Communicate()
        
        self.filtr_window=Filter_window(select_fu=self.items_fu,communication=self.communication)
        self.communication.signal.connect(self.filtr_data)
        self.filtr_window.show()
        
    #фильтрация
    def filtr_data(self, message):
        message=message.split('%')
        print(message)
        self.fill(self.items_fu(message[0],None,message[3],message[2],message[1]))

    #удалить        
    def remove(self):
        pass
    #открыть окно заказов   

    def show_selected_order_window(self,message):
        self.filtr_window.close()
        
        print(1)


    def show_orders_window(self,data):
        self.order_window=Admin_Orders_window(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu)
        self.order_window.show()

    #добавить товар в заказ
    def add_to_order(self,message):
        selected_item=self.items_fu(id=self.id_select.text())
        selected_item=selected_item[0]
        if self.create_order_item_fu(item_id=selected_item.id,order_id=1,count=int(message)):#убрать
            pass
        else:
            self.waring=warning_window('Выбранное количиство товара превышает доступный для покупки')
            self.waring.show()
            self.fill()
    #показать окно добавления
    def show_add_window(self):
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
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        
        super().__init__()
        
        self.setWindowTitle("Ваши заказы")
        self.filtr_window = None

        self.setFixedSize(900,250)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(6)
        self.fill()

        #left
        self.id_select_label=QLabel('Введите Id')
        self.id_select = QLineEdit()
        self.go_to_order_button=QPushButton('Перейти к заказу \n с выбранным Id',self)
        self.id_select_label.setFixedSize(250,15)
        self.id_select.setFixedSize(200,50)
        self.go_to_order_button.setFixedSize(200,100)

        
        #left_layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.id_select_label)
        left_layout.addWidget(self.id_select)
        left_layout.addWidget(self.go_to_order_button)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)
        self.go_to_order_button.clicked.connect(self.go_to_order)

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
    def go_to_order(self):
        self.selected_order_window=Selected_Order_window(items_fu=self.items_fu,orders_fu=self.orders_fu,users_fu=self.users_fu,order_items_fu=self.order_items_fu,add_fu=self.add_fu,del_fu=self.del_fu,number_of_order=self.id_select.text())
        self.selected_order_window.show()

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

class warning_window(QWidget):
    def __init__(self,message):
        super().__init__()
        self.warhing_label=QLabel(message)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.warhing_label)
        self.setLayout(main_layout)
        
class Selected_Order_window(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,number_of_order):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.number_of_order=number_of_order
        
        super().__init__()
        
        self.setWindowTitle("Детали вашего заказа")
        #self.filtr_window = None

        self.setFixedSize(760,400)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(450,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(4)
        self.fill()#sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

        #left
        self.id_select_label=QLabel('Введите Id')
        self.id_select = QLineEdit()
        self.remove_detail_button=QPushButton('Удалить товар с \n с выбранным Id',self)
        self.cancel_order_button=QPushButton('Отменить \n заказ',self)
        self.accept_order_button=QPushButton('Одобрить \n заказ',self)
        self.id_select_label.setFixedSize(200,10)
        self.id_select.setFixedSize(200,50)
        self.remove_detail_button.setFixedSize(200,100)
        self.cancel_order_button.setFixedSize(200,100)
        self.accept_order_button.setFixedSize(200,100)

                #конект
        self.remove_detail_button.clicked.connect(self.remove_item)
        self.cancel_order_button.clicked.connect(self.cancel_order)
        self.accept_order_button.clicked.connect(self.accept_order)

        
        #left_layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.id_select_label)
        left_layout.addWidget(self.id_select)
        left_layout.addWidget(self.remove_detail_button)
        left_layout.addWidget(self.cancel_order_button)
        left_layout.addWidget(self.accept_order_button)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        #main
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)

    def fill(self,order_items=None):

        self.table.clear()
        self.table.setHorizontalHeaderLabels([
            'id',
            'item_id',
            'order_id',
            'count',
        ])
        if order_items==None:
            order_items=self.order_items_fu(order_id=self.number_of_order)
        for j,i in enumerate(order_items):
            idd=QTableWidgetItem(str(i.id))
            item_id=QTableWidgetItem(str(i.item_id))
            sell_id=QTableWidgetItem(str(i.order_id))
            cnt=QTableWidgetItem(str(i.count))
            costil=1
            self.table.setItem(j,0,idd)
            self.table.setItem(j,1,item_id)
            self.table.setItem(j,2,sell_id)
            self.table.setItem(j,3,cnt)
    def remove_item(self):
        self.del_fu(self.order_items_fu(id=self.id_select.text())[0])
        self.fill()
    def cancel_order(self):
        self.del_fu(self.orders_fu(id=self.number_of_order)[0])
        self.close()
    def accept_order(self):
        pass
