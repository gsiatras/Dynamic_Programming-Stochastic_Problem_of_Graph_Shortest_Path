import numpy as np

class GraphAgent:
    def __init__(self, c, stages, nodes, total_nodes):
        self.stages = stages
        self.nodes = nodes
        self.total_nodes = total_nodes
        self.ci = c


        # self.ccost = np.zeros((self.total_nodes ,))  # array that holds the cost from 1 node to another (each possition is a node)
        self.d = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        # for i in range(self.stages):
        #     di = []
        #     for j in range(int(self.nodes[i])):
        #         di.append(0)
        #     self.d.append(di)

        self.cost = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        # for i in range(self.stages):
        #     costi = []
        #     for j in range(int(self.nodes[i])):
        #         costi.append(0)
        #     self.cost.append(di)
        print(self.cost)

        # self.path = np.zeros((self.total_nodes ,))

    # function to create the dynamic area
    # def dynamic_array(self):
    #     k = 1
    #     for i in range(self.total_nodes):
    #         for j in self.cost[i]:
    #             if self.cost[i][j] < 1000:
    #                 self.c[i][k] = self.cost[i][j]
    #             k += 1
    #
    #     for i in range(self.stages - 1):
    #         for j in range(int(self.nodes[i])):
    #             for k in range(int(self.nodes[i + 1])):
    #             c += 1




    def calculate(self):
        for i in range(self.stages - 2, -1, -1):
            for j in range(self.nodes[i]):
                min = 1000
                for k in range(int(self.nodes[i+1])):
                    # print('%d || %d || %d' %( i,j, k))
                    if c[i][j][k] + self.cost[i+1][k] < min:
                        min = c[i][j][k] + self.cost[i+1][k]
                        self.d[i][j] = i+1, k
                self.cost[i][j] = min
        # 3
        for i in range(self.stages):
            for j in range(int(self.nodes[i])):
                print('%d\t%d %d \t%s' % (self.cost[i][j], i, j, self.d[i][j]))





    def print_graph(self):
        c = 0
        print('Graph: \n')
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




