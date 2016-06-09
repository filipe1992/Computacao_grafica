'''
Created on 8 de jun de 2016

@author: Filipe Damasceno
'''

import sys

from PyQt4 import QtCore, QtGui


class Janela(QtGui.QWidget):
    
    def __init__(self, altura=500,largura=500):
        super(Janela, self).__init__()
        
        self.altura = altura
        self.largura = largura
        self.centro = dict({'x':(largura//20)-1,'y':(altura//20)-1})
        self.cores = [ [ QtCore.Qt.white for _ in range(5,((self.altura//10))+5)]  for _ in range((self.largura//10))]
        #self.a = None
        self.iniciarUI()
        
    
    def iniciarUI(self):
        
        self.quadrilatero = QtGui.QPushButton("Quadrilatero",self)
        self.quadrilatero.move(0,0)
        
        self.connect(self.quadrilatero,QtCore.SIGNAL("clicked()"),self.inputPontos)
        
        self.limpa = QtGui.QPushButton("limpar",self)
        self.limpa.move(100,0)
        self.connect(self.limpa,QtCore.SIGNAL("clicked()"),self.limpar)
        
        reta = QtGui.QPushButton("circulo",self)
        reta.move(200,0)
        
        self.setGeometry(300, 150, self.altura-10, self.largura+40)
        self.setWindowTitle("teste-bresham")
        self.show()
    
    def inputPontos(self):
        texto,ok = QtGui.QInputDialog.getText(self, "Retas", "entre com os pontos.\n Formato: x1,y1;x2,y2")
        if ok:
            lpontos = texto.split(sep=";")
            pontos = []
            cont = 0
            for i in lpontos:
                pontos.append(i.split(sep=","))
                pontos[cont] = [int(pontos[cont][0]),int(pontos[cont][1])]
                cont+=1
            print(pontos)
            for x in self.desenhar(pontos):
                self.desenharPonto(x[0], x[1])
            
    
    def limpar(self):
        self.limpart()

    def circulo(self):
        texto,ok = QtGui.QInputDialog.getText(self, "circulo", "entre com centro e o raio do circulo.\n Formato: c1,c2;r1,r2")
        if ok:
            lpontos = texto.split(sep=";")
            pontos = []
            cont = 0
            for i in lpontos:
                pontos.append(i.split(sep=","))
                pontos[cont] = [int(pontos[cont][0]),int(pontos[cont][1])]
                cont+=1
            print(pontos)
        
    def calcCirculo(self,pontos):
        vali,init,fim = self.colocar_origem(pontos[0], pontos[1])
        
        
        
    
    def paintEvent(self, e):
        
        self.a = QtGui.QPainter(self)
        #self.a.begin(self)
        self.Principal()
        self.a.end()
    
    def Principal(self):
        self.desenharTela()
        
        
        
        
    def desenharTela(self):
        cor = QtGui.QColor(QtCore.Qt.white)
        self.a.setPen(cor)
        
        for i in range((self.largura//10)-1):
            for j in range(5,((self.altura//10)-1)+5):
                self.a.setBrush(QtGui.QColor(self.cores[i][j-5]))
                self.a.drawRect(i*10, j*10, 10, 10)
    
    def limpart(self):
        for i in range(len(self.cores)):
            for j in range(len(self.cores[1])):
                if self.cores[i][j] != QtCore.Qt.white:
                    self.cores[i][j] = QtCore.Qt.white
        self.update()
                
        
    def desenharPonto(self,x,y):
        y=-y+self.centro['y']
        x+=self.centro['x']
        '''self.a.setBrush(QtGui.QColor(QtCore.Qt.white))
        self.a.drawRect(x*10,y*10+50,10,10)'''
        self.cores[x][y] = QtCore.Qt.black
        self.update()
    
    ''' funcoes para o trabalho'''
    
    def colocar_origem(self,ponto1,ponto2):
        return ponto1, [0,0],[ponto2[0]-ponto1[0],ponto2[1]-ponto1[1]]

    def voltar_posicao(self,ponto,val):
        return [ponto[0]+val[0],ponto[1]+val[1]]
    
    def transformar(self,ponto,posicao):
        if posicao == 2:
            return [ponto[1],ponto[0]]
        elif posicao == 3:
            return [-ponto[1],ponto[0]]
        elif posicao == 4:
            return [-ponto[0],ponto[1]]
        elif posicao == 5:
            return [-ponto[0],-ponto[1]]
        elif posicao == 6:
            return [-ponto[1],-ponto[0]]
        elif posicao == 7:
            return [ponto[1],-ponto[0]]
        elif posicao == 8:
            return [ponto[0],-ponto[1]]
        else:
            return ponto
    
    def posicao(self,ponto1,ponto2):
        
        if (ponto2[0] - ponto1[0]) != 0:
            m = (ponto2[1] - ponto1[1])/(ponto2[0] - ponto1[0])
        else:
            m = 0
        
        if ponto1[0] < ponto2[0] and 0 <= m <= 1:
            return 1
        elif ponto1[0] < ponto2[0] and 0 > m >= -1:
            return 8
        elif ponto1[0] > ponto2[0] and 0 >= m >= -1:
            return 4
        elif ponto1[0] > ponto2[0] and 0 < m <= 1: 
            return 5
        elif ponto1[1] < ponto2[1] and m < -1:
            return 3
        elif ponto1[1] < ponto2[1] and m > 1:
            return 2
        elif ponto1[1] > ponto2[1] and m < -1:
            return 7
        elif ponto1[1] > ponto2[1] and m > 1:
            return 6
    
    def bresenham(self,ponto1,ponto2):
        x = ponto1[0]
        y = ponto1[1]
        if y == ponto2[1]:
            return [[i,y] for i in range(ponto2[0])] if ponto2[0] > 0 else [[i,y] for i in range(0,ponto2[0],-1)] 
        if x == ponto2[0]:
            return [[x,i] for i in range(ponto2[1])] if ponto2[1] > 0 else [[x,i] for i in range(0,ponto2[1],-1)] 
        
        if (ponto2[0] - ponto1[0]) != 0:
            m = (ponto2[1] - ponto1[1])/(ponto2[0] - ponto1[0])
        else:
            m = 0
        e = m - 0.5
        pontos = []
        for _ in range(ponto2[0]):
            pontos.append([x,y])
            while e >= 0:
                y += 1
                e -= 1
            x += 1
            e += m
        pontos.append([x,y])
        return pontos
    
    def desenhar(self,pontos = []):
        
        retas = []
        
        for i in range(len(pontos)-1):
            p1,p2 = pontos[i],pontos[i+1]
            print("pontos: << P1: ",p1," P2: ",p2,">>")
            
            val,p1,p2 = self.colocar_origem(p1, p2)
            print("ponto de subtracao: ",val,"novos pontos: P1: ",p1," P2: ",p2)
            
            pos = self.posicao(p1, p2)
            print("Posicao no octeto: ",pos)
            p1 = self.transformar(p1, pos)
            p2 = self.transformar(p2, pos)
            if p2[0] < 0 > p2[1]:
                p2[0],p2[1] = p2[0]*-1,p2[1]*-1
            print("Pontos transformados: P1: ",p1," P2: ",p2)
            ptos = self.bresenham(p1, p2)
            print("Reta: ",ptos)
            pf = []
            for i in ptos:
                pf.append(self.voltar_posicao(self.transformar(i, pos), val))
            print("Reta na posicao de Origem: ",pf)
            print("+=+=+="*10)
            retas += pf
        return retas
    
        
        


app = QtGui.QApplication(sys.argv)
janela = Janela()
sys.exit(app.exec_())
        
        
                