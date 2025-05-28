import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def get_value(self):
        return int(self.value)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def del_neighbor(self, neighbor):
        self.neighbors.remove(neighbor)


def get_data(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')

    node1, node2 = map(int, lines[0].split())

    edges = []
    for line in lines[1:]:
        start, end = map(int, line.split('->'))
        edges.append((start, end))

    return node1, node2, edges



def swap(nodes, node1, node2):
    nodeArray = []
    line = []
    for neighbor in (nodes[node1].neighbors):
        if neighbor.get_value() != nodes[node2].get_value():
            line.append(neighbor)
    nodeArray.append(line)

    line = []
    for neighbor in (nodes[node2].neighbors):
        if neighbor.get_value() != nodes[node1].get_value():
            line.append(neighbor)
    nodeArray.append(line)


    nodes[node2].del_neighbor(nodeArray[1][1])
    (nodeArray[1][1]).del_neighbor(nodes[node2])

    nodes[node2].add_neighbor(nodeArray[0][0])
    (nodeArray[0][0]).add_neighbor(nodes[node2])

    nodes[node1].del_neighbor(nodeArray[0][0])
    (nodeArray[0][0]).del_neighbor(nodes[node1])

    nodes[node1].add_neighbor(nodeArray[1][1])
    (nodeArray[1][1]).add_neighbor(nodes[node1])


def to_string(tree):
    for node in tree:
        for child in tree[node].neighbors:
            print(f'{node}->{child.get_value()}')


def get_tree(adj_list):
    nodes = {}
    for edge in adj_list:
        parent, child = edge
        # print(parent)
        # print(edge)
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child)
        nodes[parent].add_neighbor(nodes[child])
    return nodes

# node1=5
# node2=4
# adj_list = [
# "0->4",
# "4->0",
# "1->4",
# "4->1",
# "2->5",
# "5->2",
# "3->5",
# "5->3",
# "4->5",
# "5->4",
# ]
node1, node2, adj_list = get_data("NN_dataset.txt")
nodes = get_tree(adj_list)
default = copy.deepcopy(nodes)
swap(nodes, node1, node2)
swap1 = copy.deepcopy(nodes)
swap(nodes, node1, node2)
swap2 = copy.deepcopy(nodes)
to_string(swap1)
print('')
to_string(swap2)