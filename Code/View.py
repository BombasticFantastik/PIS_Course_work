import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QLineEdit
from random import randint


class Third_Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Интерфейс с фотографиями и кнопками")
        self.setGeometry(256, 256, 512, 256)


        #создаём p и g

        self.p_label=QLabel('p:')
        self.g_label=QLabel('g:')


        #инпуты
        self.p_input=QLineEdit()
        self.g_input=QLineEdit()

        self.button_get_p = QPushButton("Создать p", self)
        self.button_get_g = QPushButton("Создать g", self)
        self.button_get_p.clicked.connect(self.on_button_get_p_clicked)
        self.button_get_g.clicked.connect(self.on_button_get_g_clicked)




        self.a_label=QLabel('а:')
        self.b_label=QLabel('b:')


        #инпуты
        self.a_input=QLineEdit()
        self.b_input=QLineEdit()
        #A и B
        self.A_label=QLabel('А:')
        self.B_label=QLabel('B:')

        #инпуты
        self.A_input=QLineEdit()
        self.B_input=QLineEdit()

        #K
        self.K_label_left=QLabel('K:')
        self.K_label_right=QLabel('K:')
        self.K_input_left=QLineEdit()
        self.K_input_right=QLineEdit()

        self.button_get_left_K = QPushButton("Создать K", self)
        self.button_get_right_K = QPushButton("Создать K", self)
        self.button_get_left_K.clicked.connect(self.on_button_get_left_K_clicked)
        self.button_get_right_K.clicked.connect(self.on_button_get_right_K_clicked)

        #кнопки для создания a и b

        self.button_get_a = QPushButton("Создать a", self)
        self.button_get_b = QPushButton("Создать b", self)
        self.button_get_a.clicked.connect(self.on_button_get_a_clicked)
        self.button_get_b.clicked.connect(self.on_button_get_b_clicked)


        #кнопки для создания A и B
        self.button_get_A = QPushButton("Создать A", self)
        self.button_get_B = QPushButton("Создать B", self)
        self.button_get_A.clicked.connect(self.on_button_get_A_clicked)
        self.button_get_B.clicked.connect(self.on_button_get_B_clicked)

        #левый
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.p_label)
        left_layout.addWidget(self.p_input)
        left_layout.addWidget(self.button_get_p)
        left_layout.addWidget(self.a_label)
        left_layout.addWidget(self.a_input)
        left_layout.addWidget(self.button_get_a)
        left_layout.addWidget(self.A_label)
        left_layout.addWidget(self.A_input)
        left_layout.addWidget(self.button_get_A)
        left_layout.addWidget(self.K_label_left)
        left_layout.addWidget(self.K_input_left)
        left_layout.addWidget(self.button_get_left_K)
        #правый
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.g_label)
        right_layout.addWidget(self.g_input)
        right_layout.addWidget(self.button_get_g)
        right_layout.addWidget(self.b_label)
        right_layout.addWidget(self.b_input)
        right_layout.addWidget(self.button_get_b)
        right_layout.addWidget(self.B_label)
        right_layout.addWidget(self.B_input)
        right_layout.addWidget(self.button_get_B)
        right_layout.addWidget(self.K_label_right)
        right_layout.addWidget(self.K_input_right)
        right_layout.addWidget(self.button_get_right_K)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

        
    #p и g
    def on_button_get_p_clicked(self):
       pass
    def on_button_get_g_clicked(self):
        pass
    #a и b
    def on_button_get_a_clicked(self):
        self.a_input.setText(str(randint(10**27,(10**28)-1)))
    def on_button_get_b_clicked(self):
        self.b_input.setText(str(randint(10**27,(10**28)-1)))

    #A и B
    def on_button_get_A_clicked(self):
        A=pow(int(self.g_input.text()),int(self.a_input.text()),int(self.p_input.text()))
        self.A_input.setText(str(A))
    def on_button_get_B_clicked(self):
        B=pow(int(self.g_input.text()),int(self.b_input.text()),int(self.p_input.text()))
        self.B_input.setText(str(B))

    #K
    def on_button_get_left_K_clicked(self):
        K=pow(int(self.B_input.text()),int(self.a_input.text()),int(self.p_input.text()))
        self.K_input_left.setText(str(K))
        #pow(B,a,p)

    def on_button_get_right_K_clicked(self):
        K=pow(int(self.A_input.text()),int(self.b_input.text()),int(self.p_input.text()))
        self.K_input_right.setText(str(K))
        
app = QApplication(sys.argv)
window = Third_Window()
window.show()
sys.exit(app.exec())