"""
SmallParsimony(T, Character)
    for each node v in tree T
        Tag(v) ← 0
        if v is a leaf
            Tag(v) ← 1
            for each symbol k in the alphabet
                if Character(v) = k
                    sk(v) ← 0
                else
                    sk(v) ← ∞
    while there exist ripe nodes in T
        v ← a ripe node in T
        Tag(v) ← 1
        for each symbol k in the alphabet
            sk(v) ← minimumall symbols i {si(Daughter(v))+αi,k} + minimumall symbols j {sj(Son(v))+αj,k}
    return minimum over all symbols k {sk(v)}
"""

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

n, adj_list = get_data("smallParsimonyData.txt")
# print(adj_list)
n=4
adj_list = [
    "4->CAAATCCC",
    "4->ATTGCGAC",
    "5->CTGCGCTG",
    "5->ATGGACGA",
    "6->4",
    "6->5",
]
newNode = 0
for entry in adj_list:
    parent, child = entry.split('->')
    parent = int(parent)
    if child.isnumeric():
        child = int(child)

    if type(child) == str:
        tree[child] = {'Children': [], 'Value': list(child)}
        seqLength = len(child)

        newNode += 1
    if parent not in tree:
        tree[parent] = {'Children': [], 'Value': []}
        if parent > maxNode:
            maxNode = parent
    tree[parent]['Children'].append(child)

score = 0
for pos in range(seqLength):
    score += SmallParsimony(tree, position=pos, root=maxNode)

print(score)

for node in tree:
    if len(tree[node]['Children']) == 0:
        continue
    parent_seq = ''.join(tree[node]['Value'])
    for child in tree[node]['Children']:
        child_seq = ''.join(tree[child]['Value'])
        diff = HammingDistance(parent_seq, child_seq)
        print(f"{parent_seq}->{child_seq}:{diff}")
        print(f"{child_seq}->{parent_seq}:{diff}")