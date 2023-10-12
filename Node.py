#인공신경망의 단일 노드를 정의하는 클래스

class Node:
    def __init__(self, connecteds, weights):
        self.connecteds = connecteds
        self.weights = weights


#인공신경망의 노드 그룹 연결을 정의하는 클래스

class NodeGroup:
    def __init__(self, firstNodes, nextGroups, weights):
        self.firstNodes = firstNodes
        self.nextGroups = nextGroups

        #다음 노드 그룹으로 연결 설정하기
        for i in range(len(self.firstNodes)):
            firstNodes[i] = Node(, weights[i])