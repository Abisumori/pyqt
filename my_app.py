from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)




from instr import *
from second_win import *
     
class MainWin(QWidget):
   def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()
       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()
       # создаём и настраиваем графические элементы:
       self.initUI()




       #устанавливает связи между элементами
       self.connects()




       # старт:
       self.show()




   def initUI(self):
       ''' создаёт графические элементы '''
       self.btn_next = QPushButton(txt_next)
       # Изменение цвета кнопки
       self.btn_next.setStyleSheet("background-color: rgb(255, 255, 255);")
       self.hello_text = QLabel(txt_hello)
       # Изменение размера и стиля шрифта
       self.hello_text.setFont(QFont("Times", 18, QFont.Bold))
       self.instruction = QLabel(txt_instruction)
       # Изменение размера и стиля шрифта
       self.instruction.setFont(QFont("Times", 12, italic=True))




       self.layout = QVBoxLayout()
       self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)        
       self.setLayout(self.layout)




 
   def next_click(self):
       self.tw = TestWin()
       self.hide()




   def connects(self):
       self.btn_next.clicked.connect(self.next_click)




   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       # Изменение цвета фона окна
       self.setStyleSheet("background-color: rgb(230, 230, 250);")
       self.resize(win_width, win_height)
       self.move(win_x, win_y)




def main():
   app = QApplication([])
   mw = MainWin()
   app.exec_()




main()
