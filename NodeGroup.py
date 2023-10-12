#인공신경망의 노드 그룹 연결을 정의하는 클래스
import numpy as np

#활성화 함수
def sigmoid(input):
    return 1 / (1 + np.exp(-input))

class NodeGroup:
    #가중치, 편향 입력받기
    def __init__(self, weights, biases):
        self.weights = weights
        self.biases = biases

    #input: numpy 배열 형태
    def forwardProp(self, input):
        x = np.copy(input)
        for i in range(len(self.weights)):
            x = (np.dot(x, self.weights[i])) + self.biases[i] #가중치 곱하고 편향 더하기
            x = sigmoid(x) #활성화 함수

        #출력값
        return x