from PyQt6.QtCore import pyqtSignal, QObject
import datetime
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit,QTableWidget,QTableWidgetItem
class Communicate(QObject):
        signal = pyqtSignal(str)


class Login_window(QWidget):
    
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,create_order_item_fu,save_fu,create_item_fu,order_user_join,create_order,get_order_items_items_join):
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
        self.save_fu=save_fu
        self.create_item_fu=create_item_fu
        self.order_user_join=order_user_join
        self.create_order=create_order
        self.get_order_items_items_join=get_order_items_items_join
        
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
        selected_user=self.users_fu(login=self.login_input.text(),password=self.password_input.text())
        
        if selected_user[0].login==self.login_input.text() and selected_user[0].password==self.password_input.text():
            print(selected_user[0].status)
            #Админ
            if selected_user[0].status=='Администратор':#??????????? как я мог себе это позволить ?
                self.admin_cat_window=Admin_Cat(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu,self.create_order_item_fu,selected_user[0].id,self.create_order,self.get_order_items_items_join)
                self.admin_cat_window.show()
                self.close()
            #Поставщик
            else:
                
                self.seller_cat_window=Seller_Cat(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu,self.create_order_item_fu,self.save_fu,self.create_item_fu,selected_user[0].id,self.order_user_join)
                self.seller_cat_window.show()
                self.close()
        else:
            pass
        
class Admin_Cat(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,create_order_item_fu,admin_id,create_order,get_order_items_items_join):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.orders_fu=orders_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.create_order_item_fu=create_order_item_fu
        self.admin_id=admin_id
        self.create_order=create_order
        self.get_order_items_items_join=get_order_items_items_join
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
        costil=0
        for i in items:

            id=QTableWidgetItem(str(i.id))
            sell_id=QTableWidgetItem(str(i.seller_id))
            name=QTableWidgetItem(str(i.name))
            art=QTableWidgetItem(str(i.article))
            price=QTableWidgetItem(str(i.price))
            cnt=QTableWidgetItem(str(i.count))

            

            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,sell_id)
            self.table.setItem(costil,2,name)
            self.table.setItem(costil,3,art)
            self.table.setItem(costil,4,price)
            self.table.setItem(costil,5,cnt)
            costil+=1

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
        self.fill(self.items_fu(seller_id=message[0],name=message[1],price=message[2],article=message[3]))
        #{self.seller_input.text()}%{self.name_input.text()}%{self.price_input.text()}%{self.art_input.text()}

    #удалить        
    def remove(self):
        pass
    #открыть окно заказов   

    def show_selected_order_window(self,message):
        self.filtr_window.close()
        
    def show_orders_window(self,data):
        self.order_window=Admin_Orders_window(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu,self.get_order_items_items_join)
        self.order_window.show()

    #добавить товар в заказ
    def add_to_order(self,message):
        selected_item=self.items_fu(id=self.id_select.text())
        selected_item=selected_item[0]
        order_id=self.which_order_should_I_make(selected_item)
        if self.create_order_item_fu(item_id=selected_item.id,order_id=order_id,count=int(message)):#убрать
            try:
                a=self.orders_fu(seller_id=selected_item.seller_id,status='Не отправленна')
                a[0].total_price+=selected_item.price
                
            except:
                self.create_order(selected_item.seller_id,self.admin_id,str(datetime.datetime.now().date()),'Не отправленна',selected_item.price*selected_item.count)
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

    def which_order_should_I_make(self,item):

        orders=self.orders_fu(status='Не отправленна')

        for order in orders:
            if order.seller_id==item.seller_id:
                return order.id
        orders_id=[i.id for i in orders]
        if len(list(orders))==0:
            orders_id.append(0)
        return max(orders_id)+1 
        #надо сделать что бы добавлялись
        
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
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,get_order_items_items_join):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.get_order_items_items_join=get_order_items_items_join
        
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
        costil=0
        for i in orders:
            id=QTableWidgetItem(str(i.id))
            sell_id=QTableWidgetItem(str(i.seller_id))
            name=QTableWidgetItem(str(i.admin_id))
            art=QTableWidgetItem(str(i.created_in))
            price=QTableWidgetItem(str(i.status))
            cnt=QTableWidgetItem(str(i.total_price))
            
            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,sell_id)
            self.table.setItem(costil,2,name)
            self.table.setItem(costil,3,art)
            self.table.setItem(costil,4,price)
            self.table.setItem(costil,5,cnt)
            costil+=1
    def go_to_order(self):
        self.selected_order_window=Selected_Order_window(items_fu=self.items_fu,orders_fu=self.orders_fu,users_fu=self.users_fu,order_items_fu=self.order_items_fu,add_fu=self.add_fu,del_fu=self.del_fu,number_of_order=self.id_select.text(),get_order_items_items_join=self.get_order_items_items_join)
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
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,number_of_order,get_order_items_items_join):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.number_of_order=number_of_order
        self.get_order_items_items_join=get_order_items_items_join
        
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
            'article',
            'price',
            'count',
        ])
        
        if order_items==None:
            order_items_with_join=self.get_order_items_items_join(order_id=self.number_of_order)
            
        costil=0
        for i in order_items_with_join:
            id=QTableWidgetItem(str(i[0].id))
            art=QTableWidgetItem(str(i[1].article))
            price=QTableWidgetItem(str(i[1].price))
            cnt=QTableWidgetItem(str(i[0].count))
            
            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,art)
            self.table.setItem(costil,2,price)
            self.table.setItem(costil,3,cnt)
            costil+=1
    def remove_item(self):
        self.del_fu(self.order_items_fu(id=self.id_select.text())[0])
        self.fill()
    def cancel_order(self):
        self.del_fu(self.orders_fu(id=self.number_of_order)[0])
        self.close()
    def accept_order(self):
        pass

#__________________________________sellers______________________________________________________:

class Seller_Cat(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,create_order_item_fu,save_fu,create_item_fu,seller_id,order_user_join):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.orders_fu=orders_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.create_order_item_fu=create_order_item_fu
        self.save_fu=save_fu
        self.create_item_fu=create_item_fu
        self.seller_id=seller_id
        self.order_user_join=order_user_join
        super().__init__()
        self.setWindowTitle("Главное окно поставщика")
        self.filtr_window = None
       

        self.setFixedSize(710,400)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(5)
        self.fill()

        #id
        self.id_select_label=QLabel('Введите Id')
        self.id_select = QLineEdit()

        #Добавить/Удалить/Найти
        self.button_change = QPushButton("Изменить информацию", self)
        self.button_orders = QPushButton("Ваши заказы", self)
        self.button_add_item=QPushButton('Добавить новый \n товар',self)
        self.button_change.setFixedSize(170,100) 
        self.button_orders.setFixedSize(170,100)  
        self.button_add_item.setFixedSize(170,100)     

        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.id_select_label)
        left_layout.addWidget(self.id_select)
        left_layout.addWidget(self.button_change)
        left_layout.addWidget(self.button_orders)
        left_layout.addWidget(self.button_add_item)

        #table
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)
        #конект
        self.button_change.clicked.connect(self.show_change_window)
        self.button_orders.clicked.connect(self.show_orders_window)
        self.button_add_item.clicked.connect(self.show_add_window)


        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)

    #заполнение данных в таблицу
    def fill(self,items=None):
        self.table.clear()
        self.table.setHorizontalHeaderLabels([
            'id',
            'name',
            'article',
            'price',
            'count',
        ])
        if items==None:
            items=self.items_fu(seller_id=self.seller_id)
        costil=0
        for i in items:

            id=QTableWidgetItem(str(i.id))
            name=QTableWidgetItem(str(i.name))
            art=QTableWidgetItem(str(i.article))
            price=QTableWidgetItem(str(i.price))
            cnt=QTableWidgetItem(str(i.count))

            

            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,name)
            self.table.setItem(costil,2,art)
            self.table.setItem(costil,3,price)
            self.table.setItem(costil,4,cnt)
            costil+=1

    #окно изменений
    def show_change_window(self):
        self.communication = Communicate()
        self.filtr_window=Change_window(select_fu=self.items_fu,communication=self.communication,save_fu=self.save_fu,item_id=self.id_select.text())
        self.communication.signal.connect(self.update_item)
        self.filtr_window.show()
        
    #обновляем данные в таблицы
    def update_item(self, message):
        self.fill()

    #удалить        
    def remove(self):
        pass
    #открыть окно заказов   

    def show_selected_order_window(self,message):
        self.filtr_window.close()
        
    def show_orders_window(self,data):
        self.order_window=Seller_orders_window(self.items_fu,self.orders_fu,self.users_fu,self.order_items_fu,self.add_fu,self.del_fu,self.seller_id,self.order_user_join,self.save_fu)
        self.order_window.show()

    #добавить товар
    def add_to_order(self,message):
        self.fill()
    #показать окно добавления
    def show_add_window(self):
        self.communication = Communicate()
        self.add_window=Seller_add_window(self.communication,self.create_item_fu,self.seller_id)
        self.communication.signal.connect(self.add_to_order)
        self.add_window.show()
 
class Change_window(QWidget):
    
    def __init__(self,select_fu,communication,save_fu,item_id):
        super().__init__()
        self.select_fu=select_fu
        self.con=communication
        self.save_fu=save_fu
        self.item_id=item_id
        
        
        
    
        #labels
        self.name_label=QLabel('name')
        self.price_label=QLabel('price')
        self.art_label=QLabel('art')
        self.count_label=QLabel('count')

        #inputs

        self.name_input=QLineEdit()
        self.price_input=QLineEdit()
        self.art_input=QLineEdit()
        self.count_input=QLineEdit()
        

        #labels_layout
        labels_layout = QVBoxLayout()
        labels_layout.addWidget(self.name_label)
        labels_layout.addWidget(self.price_label)
        labels_layout.addWidget(self.art_label)
        labels_layout.addWidget(self.count_label)

        #inputs_labels
        input_layout=QVBoxLayout()

        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.price_input)
        input_layout.addWidget(self.art_input)
        input_layout.addWidget(self.count_input)
        #button
        self.change_button=QPushButton("Изменить")
        self.change_button.clicked.connect(self.change_item)
        

        

        main_layout = QHBoxLayout()
        main_layout.addLayout(labels_layout)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.change_button)
        self.setLayout(main_layout)
    def change_item(self):
        item=self.select_fu(id=self.item_id)[0]
        if self.name_input.text()!='':
            item.name=self.name_input.text()

        if self.price_input.text()!='':
            item.price=self.price_input.text()

        if self.art_input.text()!='':
            item.article=self.art_input.text()

        if self.count_input.text()!='':
            item.count=self.count_input.text()

        self.save_fu()

        self.con.signal.emit('')

class Seller_add_window(QWidget):
    
    def __init__(self,communication,create_item_fu,seller_id):
        super().__init__()
        self.con=communication
        self.create_item_fu=create_item_fu
        self.seller_id=seller_id
        
        #labels
        self.name_label=QLabel('name')
        self.price_label=QLabel('price')
        self.art_label=QLabel('art')
        self.count_label=QLabel('count')

        #inputs
        self.name_input=QLineEdit()
        self.price_input=QLineEdit()
        self.art_input=QLineEdit()
        self.count_input=QLineEdit()
        

        #labels_layout
        labels_layout = QVBoxLayout()
        labels_layout.addWidget(self.name_label)
        labels_layout.addWidget(self.price_label)
        labels_layout.addWidget(self.art_label)
        labels_layout.addWidget(self.count_label)

        #inputs_labels
        input_layout=QVBoxLayout()

        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.price_input)
        input_layout.addWidget(self.art_input)
        input_layout.addWidget(self.count_input)
        #button
        self.add_button=QPushButton("Добавить новый товар")
        self.add_button.clicked.connect(self.add_item)
        

        

        main_layout = QHBoxLayout()
        main_layout.addLayout(labels_layout)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.add_button)
        self.setLayout(main_layout)
    def add_item(self):
        self.create_item_fu(seller_id=self.seller_id,name=self.name_input.text(),price=self.price_input.text(),article=self.art_input.text(),count=self.count_input.text())
        self.con.signal.emit('')

class Seller_orders_window(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,seller_id,join_fu,save_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.seller_id=seller_id
        self.join_fu=join_fu
        self.save_fu=save_fu
        
        super().__init__()
        
        self.setWindowTitle("Ваши заказы")
        self.filtr_window = None

        self.setFixedSize(800,250)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(655,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(5)
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
            'admin',
            'total price',
            'status',
            'address',
        ])
        if orders==None:
            orders=self.join_fu(seller_id=self.seller_id)
        costil=0
        for i in orders:
            id=QTableWidgetItem(str(i[0].id))
            admin_name=QTableWidgetItem(str(i[1].legal_entity))
            total_price=QTableWidgetItem(str(i[0].total_price))
            status=QTableWidgetItem(str(i[0].status))
            address=QTableWidgetItem(str(i[1].address))
            self.table.setItem(costil,0,id)
            self.table.setItem(costil,1,admin_name)
            self.table.setItem(costil,2,total_price)
            self.table.setItem(costil,3,status)
            self.table.setItem(costil,4,address)
            costil+=1
    def go_to_order(self):
        self.selected_order_window=Selected_Sellers_order_window(items_fu=self.items_fu,orders_fu=self.orders_fu,users_fu=self.users_fu,order_items_fu=self.order_items_fu,add_fu=self.add_fu,del_fu=self.del_fu,number_of_order=self.id_select.text(),save_fu=self.save_fu)
        self.selected_order_window.show()

class Selected_Sellers_order_window(QWidget):
    def __init__(self,items_fu,orders_fu,users_fu,order_items_fu,add_fu,del_fu,number_of_order,save_fu):
        self.items_fu=items_fu
        self.orders_fu=orders_fu
        self.users_fu=users_fu
        self.order_items_fu=order_items_fu
        self.add_fu=add_fu
        self.del_fu=del_fu
        self.number_of_order=number_of_order
        self.save_fu=save_fu
        
        super().__init__()
        
        self.setWindowTitle("Детали выбранного заказа")
        #self.filtr_window = None

        self.setFixedSize(760,400)

        #table
        self.table = QTableWidget()
        self.table.setFixedSize(450,387)
        self.table.setRowCount(25)
        self.table.setColumnCount(4)
        self.fill()#sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

        self.cancel_order_button=QPushButton('Отменить \n заказ',self)
        self.accept_order_button=QPushButton('Одобрить \n заказ',self)
        self.cancel_order_button.setFixedSize(200,100)
        self.accept_order_button.setFixedSize(200,100)

                #конект
        self.cancel_order_button.clicked.connect(self.cancel_order)
        self.accept_order_button.clicked.connect(self.accept_order)

        
        #left_layout
        left_layout = QVBoxLayout()
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

    def cancel_order(self):
        self.del_fu(self.orders_fu(id=self.number_of_order)[0])
        self.close()
    def accept_order(self):
        obj=self.orders_fu(id=self.number_of_order)[0]
        obj.status='Одобренна'
        self.save()