# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# img = mpimg.imread("cartas-3.jpeg")
# imgplot = plt.imshow(img)
# plt.show()

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# img=mpimg.imread('your_image.png')
# imgplot = plt.imshow(img)
# plt.show()


## importing Image class from PIL package  
#from PIL import Image  
#import time
#
#  
## creating a object  
## im = Image.open(open("/home/rage1452/Documents/repos/Lottery/logo.png",'rb'))
#im = Image.open(open("logo.png",'rb'))  
#  
#im.show()
## time.sleep(30) 

 # Filename: signals_slots.py

 #"""Signals and slots example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

 ###
 #from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 #label = QLabel(self)
 # pixmap = QPixmap('cartas-3.jpeg')
 #label.setPixmap(pixmap)

 # Optional, resize window to image size
 #self.resize(pixmap.width(),pixmap.height())

 ####

from random import seed
from random import choice

#Init list
TotalCards = 54
Deck = [i for i in range(1,TotalCards+1)]
DrawnCards = []

def greeting():
     """Slot function."""
     if msg.text():
         msg.setText("")
     else:
         msg.setText("Hello World!")

def DRAWNEWCARD():
    if(Deck):
        CardDrawn = choice(Deck)
        # print(CardDrawn)
        msg.setText(str(CardDrawn))
        msg.update()
        
        pixmap = QPixmap('cards/'+str(CardDrawn)+'.png')
        lblImg.setPixmap(pixmap)
        lblImg.update()

        DrawnCards.append(CardDrawn)
        Deck.remove(CardDrawn)
        # print(Deck)
        print('Drawn Cards: ')
        print(DrawnCards)
    else:
        msg.setText("Finished!!!")
        msg.update()


def STARTGAME():
    #Init list
    global Deck
    global DrawnCards
    Deck = [i for i in range(1,TotalCards+1)]
    DrawnCards = []
    pixmap = QPixmap('logo.jpg')
    lblImg.setPixmap(pixmap)
    msg.setText('')
    msg.update()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Loteria')
layout = QVBoxLayout()

btnNewGame = QPushButton('New Game')
btnNewGame.clicked.connect(STARTGAME)  # Connect clicked to greeting()
layout.addWidget(btnNewGame)

btn = QPushButton('Draw Card')
btn.clicked.connect(DRAWNEWCARD)  # Connect clicked to greeting()
layout.addWidget(btn)

msg = QLabel('')

lblImg = QLabel('')
pixmap = QPixmap('logo.jpg')
lblImg.setPixmap(pixmap)

layout.addWidget(msg)
layout.addWidget(lblImg)
window.setLayout(layout)
window.resize(480,720)
# window.update()
# window.resize(pixmap.width(),pixmap.height())
 #self.resize(pixmap.width(),pixmap.height())
window.update()
window.show()
sys.exit(app.exec_())