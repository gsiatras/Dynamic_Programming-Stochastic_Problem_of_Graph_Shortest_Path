import numpy as np

class GraphAgent:
    def __init__(self, c, stages, nodes):
        self.stages = stages
        self.nodes = nodes
        self.ci = c

        self.d = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        self.cost = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        self.path = [0 for j in range(self.stages)]
        # print(self.cost)

    def printer(self):
        print('============================Graph===============================')
        self.print_graph()
        print('================================================================')
        print('------------------Path and cost for every node------------------')
        # print path and cost for every node
        print('Current: \t\t\t To: \nStage:\tNode:\t\tStage:\tNodes:\tCost to end:')
        for i in range(self.stages - 1):
            for j in range(int(self.nodes[i])):
                print(' %d\t\t %d\t\t\t %d\t\t %d\t\t %d' % (i, j, i + 1, self.d[i][j], self.cost[i][j]))
        print('================================================================')
        print('------------------Shortest Path and cost to end-----------------')
        for k in range(self.stages):
            if k == self.stages - 1:
                print('(%d, %d)' % (k, self.path[k]))
            else:
                print('(%d, %d) =>'  % (k, self.path[k]))
        print('Total cost: %d' % self.cost[0][0])

    #  function to calculate sortest path
    def calculate(self):
        for i in range(self.stages - 2, -1, -1):
            for j in range(self.nodes[i]):
                min = 1000
                for k in range(int(self.nodes[i+1])):
                    # print('%d || %d || %d' %( i,j, k))
                    if c[i][j][k] + self.cost[i+1][k] < min:
                        min = c[i][j][k] + self.cost[i+1][k]
                        self.d[i][j] = k
                self.cost[i][j] = min
        # find sortest path
        self.path[0] = 0
        for i in range(1, self.stages):
            self.path[i]= self.d[i-1][self.path[i-1]]
        # print(self.d)
        # print results
        self.printer()
        # print(self.path)

    def print_graph(self):
        print('Current: \t\t\t To: \nStage:\t Node:\t\t Stage:\t Node:\t Cost:')
        for i in range(self.stages - 1):
            for j in range(int(self.nodes[i])):
                for k in range(int(self.nodes[i + 1])):
                    print('%d\t\t %d\t\t\t %d\t\t %d\t\t %d' % (i, j, i + 1, k, self.ci[i][j][k]))

def menu():
    stages = int(input('Stages: \n'))
    nodes = []
    nodes.append(1)
    c = []

    for i in range(1, stages):
        nodes.append(int(input('Nodes for stage %d:' % i)))
    for i in range(stages - 1):
        cost = []
        for j in range(int(nodes[i])):
            node_cost = []
            for k in range(int(nodes[i+1])):
                node_cost.append(int(input('Cost from Stage %d Node %d to Stage %d Node %d:' % (i, j, i + 1, k))))
            cost.append(node_cost)
        c.append(cost)
    return c, stages, nodes



if __name__ == '__main__':
    # c, stages, nodes= menu()
    # graph1
    c = [[[2, 3]], [[5, 1, 1000], [1000, 1000, 3]], [[6, 1000], [3, 2], [1000, 4]]]
    stages = 4
    nodes = [1, 2, 3, 2]
    # ipnut graph
    stages = 7
    nodes = [1, 3, 3, 3, 4, 3, 2]
    c =[[[5, 7, 4]],
        [[2, 1000, 1000], [1000, 3, 4], [6, 7, 5]],
        [[7, 2, 1000], [3, 1, 2], [1000, 4, 2]],
        [[4, 2, 1000, 6], [1000, 3, 1000, 1000], [5, 1000, 2, 4]],
        [[5, 1000, 4], [1000, 6, 1000], [1000, 3, 1000], [1000, 1000, 3]],
        [[7, 4], [8, 5], [6, 7]]]
    agent = GraphAgent(c, stages, nodes)
    agent.calculate()





