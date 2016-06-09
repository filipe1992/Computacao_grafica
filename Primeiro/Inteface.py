'''
Created on 4 de jun de 2016

@author: Filipe Damasceno
'''

import sys
from PyQt4 import  QtGui, QtCore

class Interface(QtGui.QWidget):
    
    def __init__(self,largura = 500, altura = 500, pontos = [[1,2],[2,3],[3,4],[4,5]]):
        super(Interface, self).__init__()
        
        self.altura =  altura
        self.largura = largura
        self.pontos = pontos
        self.initUI()
        
    def initUI(self):
        
        quadrilatero = QtGui.QPushButton("Quadrilatero",self)
        quadrilatero.move(0,0)
        
        triangulo = QtGui.QPushButton("Triangulo",self)
        triangulo.move(80,0)
        
        reta = QtGui.QPushButton("Reta",self)
        reta.move(160,0)

        self.setGeometry(300, 150, self.largura, self.altura+5)
        self.setWindowTitle('bresenham')
        self.show()
    
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        #qp.end()
        
    
    
    def drawRectangles(self, qp):
        
        color = QtGui.QColor(QtCore.Qt.black)
        qp.setPen(color)
        
        for i in range(self.largura):
            for j in range(5,self.altura+5):
                if [i,j] in self.pontos:
                    qp.setBrush(QtGui.QColor(QtCore.Qt.white))
                else:
                    qp.setBrush(QtGui.QColor(QtCore.Qt.black))
                qp.drawRect(i*10, j*10, 10, 10)
         
    