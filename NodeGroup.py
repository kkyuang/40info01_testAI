#인공신경망의 노드 그룹 연결을 정의하는 클래스

class NodeGroup:
    #가중치, 편향 입력받기
    def __init__(self, weights, biases):
        self.weights = weights
        self.biases = biases