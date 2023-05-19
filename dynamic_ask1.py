import numpy as np


class GraphAgent:
    def __init__(self, c, stages, nodes, slipp):
        self.stages = stages
        self.nodes = nodes
        self.c = c
        self.p = 1 - slipp
        self.slipp = slipp
        self.pflag = 0      # flag to know if we have more than 1 possible edge so we have slip prob
        self.minCost = 0

        self.d = [[0 for k in range(self.nodes[j])] for j in range(self.stages)]
        self.path = [0 for j in range(self.stages)]
        # print(self.cost)

    def printer(self):
        print('============================Graph===============================')
        self.print_graph()
        print('================================================================')
        print('------------------Optimal path for every node------------------')
        # print path and cost for every node
        print('Current: \t\t\t To: \nStage:\tNode:\t\tStage:\tNode:')
        for i in range(self.stages - 1):
            for j in range(int(self.nodes[i])):
                print(' %d\t\t %d\t\t\t %d\t\t %d' % (i, j, i + 1, self.d[i][j]))
        print('================================================================')
        print('------------------Optimal Path and cost to end-----------------')
        for k in range(self.stages):
            if k == self.stages - 1:
                print('(%d, %d)' % (k, self.path[k]))
            else:
                print('(%d, %d) =>' % (k, self.path[k]))
        print('Min cost: %d' % self.minCost)

    # function to find slip per route per stage
    def findpslip(self, stage, node):
        i = 0
        m = 1000
        for k in range(int(self.nodes[stage + 1])):
            if (self.c[stage][node][k] < 1000):
                i += 1
                if(self.c[stage][node][k] < m):
                    m = c[stage][node][k]
                    best = k

        if i > 1:
            self.pflag = 1
            pslipp = self.slipp/(i-1)
        else:
            self.pflag = 0
            pslipp = 1

        return pslipp, best

    #  function to calculate sortest path
    def calculate(self):
        # initialize temp value function arrays
        Vtrans = [[[0 for l in range(self.nodes[j + 1])] for k in range(self.nodes[j])] for j in
                       range(self.stages - 1)]  # array to store the Value of moving from one node to another

        Vnode = [[0 for k in range(self.nodes[j])] for j in
                      range(self.stages)]  # array to store the value of each node

        for i in range(self.stages - 2, -1, -1):
            for j in range(self.nodes[i]):
                pslip, best = self.findpslip(i, j)
                # calculate transition value for each node to the next
                for k in range(int(self.nodes[i+1])):
                    total_v = 0
                    # print('%d || %d || %d' %( i,j, k))
                    # 1000 = not route available
                    if self.c[i][j][k] == 1000:
                        Vtrans[i][j][k] = float('inf')
                        continue
                    # if flag raised then we have multiple possible routes
                    if self.pflag == 1:
                        if k == best:
                            Vtrans[i][j][k] = Vnode[i + 1][k] + self.c[i][j][k] * (1 - self.p)
                            total_v = Vtrans[i][j][k]
                        else:
                            Vtrans[i][j][k] = Vnode[i + 1][k] + self.c[i][j][k] * (1 - pslip)
                            total_v = Vtrans[i][j][k]
                    else:
                        Vtrans[i][j][k] = Vnode[i + 1][k] + self.c[i][j][k]
                        total_v += Vtrans[i][j][k]
                    # the value of the node
                    Vnode[i][j] += total_v
                self.d[i][j] = np.argmin(Vtrans[i][j][:])

        # find best path
        self.path[0] = 0
        for i in range(0, self.stages-1):
            self.path[i+1] = np.argmin(Vtrans[i][self.path[i]][:])
            self.minCost += self.c[i][self.path[i]][self.path[i+1]]
        # print(self.d)
        # print results
        self.printer()
        # print(self.path)
    def print_graph(self):
        print('Current: \t\t\t To: \nStage:\t Node:\t\t Stage:\t Node:\t Cost:')
        for i in range(self.stages - 1):
            for j in range(int(self.nodes[i])):
                for k in range(int(self.nodes[i + 1])):
                    if self.c[i][j][k] < 1000:
                        print('%d\t\t %d\t\t\t %d\t\t %d\t\t %d' % (i, j, i + 1, k, self.c[i][j][k]))

def menu():
    stages = int(input('Stages: \n'))
    nodes = []
    nodes.append(1)
    c = []
    p = -1

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
    while p<0 or p>=1 :
        slipp = float(input('Slip probability between[0,1): '))

    return c, stages, nodes, slipp


if __name__ == '__main__':
    # c, stages, nodes, p= menu()

    # -----------------------------------------------------------------------------------------------------------------
    # test graph1
    # slipp = 0.2
    # c = [[[2, 3]], [[5, 1, 1000], [1000, 1000, 3]], [[6, 1000], [3, 2], [1000, 4]]]
    # stages = 4
    # nodes = [1, 2, 3, 2]
    # -----------------------------------------------------------------------------------------------------------------
    # input graph of exercise 1
    # slipp = 0.2
    # stages = 7
    # nodes = [1, 3, 3, 3, 4, 3, 2]
    # c =[[[5, 7, 4]],
    #     [[2, 1000, 1000], [1000, 3, 4], [6, 7, 5]],
    #     [[7, 2, 1000], [3, 1, 2], [1000, 4, 2]],
    #     [[4, 2, 1000, 6], [1000, 3, 1000, 1000], [5, 1000, 2, 4]],
    #     [[5, 1000, 4], [1000, 6, 1000], [1000, 3, 1000], [1000, 1000, 3]],
    #     [[7, 4], [8, 5], [6, 7]]]
    # -----------------------------------------------------------------------------------------------------------------
    # input for exercise 3
    slipp = 0.4
    stages = 7
    nodes = [1, 3, 3, 3, 5, 3, 2]
    c = [[[5, 7, 4]],
         [[2, 4, 1000], [6, 3, 4], [1000, 7, 5]],
         [[7, 2, 1000], [3, 1, 2], [1000, 4, 2]],
         [[3, 4, 2, 1000, 1000], [1000, 3, 4, 2, 1000], [1000, 1000, 5, 3, 4]],
         [[5, 1000, 1000], [5, 4, 1000], [6, 5, 3], [1000, 4, 2], [1000, 1000, 5]],
         [[6, 1000], [8, 5], [6, 7]]]
    agent = GraphAgent(c, stages, nodes, slipp)
    agent.calculate()

    while True:
        print('============================New graph===========================')
        c, stages, nodes = menu()
        agent = GraphAgent(c, stages, nodes)
        agent.calculate()






