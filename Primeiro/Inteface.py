'''
Created on 4 de jun de 2016

@author: Filipe Damasceno
'''

import sys
from PyQt4 import  QtGui, QtCore

class Interface(QtGui.QWidget):
    
    def __init__(self,largura = 500, altura = 500, pontos = [[1,2],[2,3],[3,4],[4,5]]):
        super(Interface, self).__init__()
        
        self.largura = largura
        self.altura = altura
        self.pontos = pontos
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 150, self.altura, self.largura)
        self.setWindowTitle('bresenham')
        self.show()
    
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        
        color = QtGui.QColor(QtCore.Qt.black)
        #color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        
        for i in range(self.altura):
            for j in range(self.largura):
                if [i,j] in self.pontos:
                    qp.setBrush(QtGui.QColor(QtCore.Qt.white))
                    qp.drawRect(i*10, j*10, 10, 10)
                else:
                    qp.setBrush(QtGui.QColor(QtCore.Qt.black))
                    qp.drawRect(i*10, j*10, 10, 10)             
            
    
'''def main():
    [[-4+24,3+24],[0+24,5+24],[3+24,3+24],[5+24,0+24],[0+24,-3+24],[-5+24,-1+24]]
    
    app = QtGui.QApplication(sys.argv)
    ex = Interface(pontos=bres.desenhar([[-4+24,3+24],[0+24,5+24],[3+24,3+24],[5+24,0+24],[0+24,-3+24],[-5+24,-1+24]]))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() '''