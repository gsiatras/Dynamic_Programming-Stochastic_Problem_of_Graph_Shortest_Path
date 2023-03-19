import numpy as np

class GraphAgent:
    def __init__(self, c, stages, nodes, total_nodes):
        self.stages = stages
        self.nodes = nodes
        self.total_nodes = total_nodes
        self.ci = c

        self.d = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        self.cost = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        self.path = [0 for j in range(self.stages)]
        # print(self.cost)

        # self.path = np.zeros((self.total_nodes ,))

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
        print(self.d)
        # print result
        print('Current: \t\t\t To: \nStage:\tNode:\t\tStage:\tNodes:\tCost to end:')
        for i in range(self.stages):
            for j in range(int(self.nodes[i])):
                print(' %d\t\t %d\t\t\t %d\t\t %d\t\t %d' % (i, j, i+1, self.d[i][j], self.cost[i][j]))
        print(self.path)

    def print_graph(self):
        c = 0
        print('Graph: ')
        print('Current: \t\t\t To: \nStage:\t Node:\t\t Stage:\t Node:\t Cost:')
        for i in range(self.stages - 1):
            for j in range(int(self.nodes[i])):
                for k in range(int(self.nodes[i + 1])):
                    print('%d\t\t %d\t\t\t %d\t\t %d\t\t %d' % (i, j, i + 1, k, self.ci[i][j][k]))

def menu():
    stages = int(input('Stages: \n'))
    nodes = []
    nodes.append(1)
    num_nodes = 1
    c = []

    for i in range(1, stages):
        nodes.append(int(input('Nodes for stage %d:' % i)))
        num_nodes += nodes[i]
    for i in range(stages - 1):
        cost = []
        for j in range(int(nodes[i])):
            node_cost = []
            for k in range(int(nodes[i+1])):
                node_cost.append(int(input('Cost from Stage %d Node %d to Stage %d Node %d:' % (i, j, i + 1, k))))
            cost.append(node_cost)
        c.append(cost)
    return c, stages, nodes, num_nodes



if __name__ == '__main__':
    # c, stages, nodes, num_nodes = menu()
    c = [[[2, 3]], [[5, 1, 1000], [1000, 1000, 3]], [[6, 1000], [3, 2], [1000, 4]]]
    stages = 4
    nodes = [1, 2, 3, 2]
    num_nodes = 9
    agent = GraphAgent(c, stages, nodes, num_nodes)
    agent.print_graph()
    agent.calculate()
    print('==========================================================================')




