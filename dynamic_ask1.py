import numpy as np

class GraphAgent:
    def __init__(self, c, stages, nodes,total_nodes):
        self.stages = stages
        self.nodes = nodes
        self.total_nodes = total_nodes
        self.ci = c

        # self.c = np.full((self.total_nodes, self.total_nodes),1000)
        # self.ccost = np.zeros((self.total_nodes ,))  # array that holds the cost from 1 node to another (each possition is a node)
        # self.d = np.zeros((self.total_nodes ,))
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
        self.cost[self.total_nodes] = 0
        for i in range(self.total_nodes - 1, 1, -1):
            min = 1000


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
    nodes = np.zeros((stages,))
    nodes[0] = 1
    num_nodes = 1
    c = []

    for i in range(1, stages):
        nodes[i] = int(input('Nodes for stage %d:' %i))
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
    c, stages, nodes, num_nodes = menu()
    agent = GraphAgent(c, stages, nodes, num_nodes)
    agent.print_graph()
    print('==========================================================================')




