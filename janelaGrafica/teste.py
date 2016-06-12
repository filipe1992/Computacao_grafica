'''
Created on 9 de jun de 2016

@author: Filipe Damasceno
'''
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MyFrame(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        
        self.scene=QGraphicsScene(self)
        self.scene.setSceneRect(QRectF(0,0,245,245))
        self.bt=QPushButton("Press",self)
        self.bt.setGeometry(QRect(450, 150, 90, 30))
        self.color = QColor(Qt.green)
        self.show()
        self.connect(self.bt, SIGNAL("clicked()"), self.changecolor)

    def paintEvent(self, event=None):
        paint=QPainter(self)
        paint.setPen(QPen(QColor(Qt.red),1,Qt.SolidLine))
        paint.setBrush(self.color)
        paint.drawEllipse(190,190, 70, 70)

    def changecolor(self):
        self.color = QColor(Qt.red)
        self.update()

app=QApplication(sys.argv)
f=MyFrame()
f.show()
app.exec_()