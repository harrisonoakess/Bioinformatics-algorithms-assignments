def get_root(tree, maxNode):
    largest = maxNode
    secondLargest = 0
    for node in tree:

        if isinstance(node, int):
            if (node > secondLargest) and node != largest:
                secondLargest = node

    root = largest + 1
    tree[root] = {'Children': [], 'Value': []}
    tree[root]['Children'].append(largest)
    tree[root]['Children'].append(secondLargest)

    tree[largest]['Children'].remove(secondLargest)
    tree[secondLargest]['Children'].remove(largest)

    def rem_parent(node):
        if node not in tree:
            return

        for child in tree[node]['Children']:
            if node in tree[child]['Children']:
                tree[child]['Children'].remove(node)

            rem_parent(child)

    for parentNode in [largest, secondLargest]:
        rem_parent(parentNode)

    return root


def HammingDistance(s, t):
    distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1
    return distance


def SmallParsimony(tree, position, root):
    for v in tree:
        tree[v]['Tag'] = 0
        if len(tree[v]['Children']) == 0:
            tree[v]['Tag'] = 1
            tree[v]['sk'] = {}
            for k in 'AGCT':
                if tree[v]['Value'][position] == k:
                    tree[v]['sk'][k] = 0
                else:
                    tree[v]['sk'][k] = float('inf')
    while True:
        ripeNode = None
        for v in tree:
            if tree[v]['Tag'] == 0 and len(tree[v]['Children']) > 0:
                all_children_tagged = True
                for child in tree[v]['Children']:
                    if tree[child]['Tag'] != 1:
                        all_children_tagged = False
                        break
                if all_children_tagged:
                    ripeNode = v
                    break
        if ripeNode is None:
            break

        tree[ripeNode]['Tag'] = 1
        tree[ripeNode]['sk'] = {}

        # for each character k in the alphabet
        for k in 'AGCT':
            total = 0
            for child in tree[ripeNode]['Children']:
                min_cost = float('inf')
                for l in 'AGCT':
                    if k == l:
                        delta = 0
                    else:
                        delta = 1
                    cost = tree[child]['sk'][l] + delta
                    if cost < min_cost:
                        min_cost = cost
                total += min_cost
            tree[ripeNode]['sk'][k] = total

    def reverse(v, parent=None):
        if 'Value' not in tree[v]:
            tree[v]['Value'] = []
        if parent is None:
            min_sk = min(tree[v]['sk'].values())
            min_chars = []
            for k in 'AGCT':
                if tree[v]['sk'][k] == min_sk:
                    min_chars.append(k)

            current_char = min_chars[0]
        else:
            min_cost = float('inf')
            min_chars = []
            for k in 'AGCT':
                if k == parent:
                    delta = 0
                else:
                    delta = 1
                cost = tree[v]['sk'][k] + delta
                if cost < min_cost:
                    min_cost = cost
                    min_chars = [k]
                elif cost == min_cost:
                    min_chars.append(k)
            current_char = min_chars[0]
        if len(tree[v]['Value']) <= position:
            tree[v]['Value'].append(current_char)
        else:
            tree[v]['Value'][position] = current_char
        for child in tree[v]['Children']:
            reverse(child, current_char)

    reverse(root)
    return min(tree[root]['sk'].values())


def get_data(path):
    with open(path) as f:
        lines = []
        for l in f:
            stripped = l.strip()
            lines.append(stripped)
    n_rows = int(lines[0])
    return n_rows, lines[1:]


tree = {}
edges = []
maxNode = 0
seqLength = 0

n, adj_list = get_data("unrootedParsimony.txt")
# print(adj_list)
# n=4
# adj_list = [
#     "TCGGCCAA->4",
#     "4->TCGGCCAA",
#     "CCTGGCTG->4",
#     "4->CCTGGCTG",
#     "CACAGGAT->5",
#     "5->CACAGGAT",
#     "TGAGTACC->5",
#     "5->TGAGTACC",
#     "4->5",
#     "5->4",
# ]
newNode = 0
visited_edges = set()
for entry in adj_list:
    left, right = entry.split('->')

    # parse left end
    if left.isdigit():
        u = int(left)
    else:
        u = left

    if right.isdigit():
        v = int(right)
    else:
        v = right

    if u not in tree:
        tree[u] = {'Children': [], 'Value': []}
        if not left.isdigit():
            tree[u]['Value'] = list(u)
            seqLength = len(u)

    # same for v
    if v not in tree:
        tree[v] = {'Children': [], 'Value': []}
        if not right.isdigit():
            tree[v]['Value'] = list(v)
            seqLength = len(v)

    if left.isdigit():
        num = int(left)
        if num > maxNode:
            maxNode = num
    if right.isdigit():
        num = int(right)
        if num > maxNode:
            maxNode = num
    edge_visit = tuple(sorted((u, v), key=str))
    if edge_visit in visited_edges:
        continue#connection already in set... skip
    visited_edges.add(edge_visit)
    

    tree[u]['Children'].append(v)
    tree[v]['Children'].append(u)

score = 0
root = get_root(tree, maxNode)

for pos in range(seqLength):
    score += SmallParsimony(tree, position=pos, root=root)

print(score)

# print(visited_edges)

# print(tree)
for u, v in visited_edges:
    seq_left = ''.join(tree[u]['Value'])
    seq_right = ''.join(tree[v]['Value'])
    d = HammingDistance(seq_left, seq_right)

    print(f"{seq_left}->{seq_right}:{d}")
    print(f"{seq_right}->{seq_left}:{d}")