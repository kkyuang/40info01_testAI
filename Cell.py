#세포 개체를 정의하는 파이썬 코드
import Gene
import NN
import numpy as np
import math

#시간 간격
dt = 0.01

class Cell:
    #gene: Gene 형
    #position: np.array 형
    def __init__(self, gene, position, mass):
        #변수 선언하기
        self.gene = gene
        #신경망
        self.nn = NN.geneToNN(gene)
        
        #초기 위치
        self.position = position
        #초기 속도
        self.velocity = np.array([0, 0])
        #초기 크기
        self.mass = mass
        self.size = math.sqrt(mass)

    #DPinfo: 외부 정보를 격자 형태로 전달.
    def refreshPosition(self, DPinfo):
        self.velocity = self.nn.CalcVelocity(self.velocity, self.size, DPinfo)
        self.position += self.velocity * dt