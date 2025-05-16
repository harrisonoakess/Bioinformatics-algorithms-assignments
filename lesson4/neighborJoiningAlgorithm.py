import sys
"""
NeighborJoining(D)
    n ← number of rows in D
    if n = 2
        T ← tree consisting of a single edge of length D1,2
        return T
    D* ← neighbor-joining matrix constructed from the distance matrix D
    find elements i and j such that D*i,j is a minimum non-diagonal element of D*
    Δ ← (TotalDistanceD(i) - TotalDistanceD(j)) /(n - 2)
    limbLengthi ← (1/2)(Di,j + Δ)
    limbLengthj ← (1/2)(Di,j - Δ)
    add a new row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j) for any k
    D ← D with rows i and j removed
    D ← D with columns i and j removed
    T ← NeighborJoining(D)
    add two new limbs (connecting node m with leaves i and j) to the tree T
    assign length limbLengthi to Limb(i)
    assign length limbLengthj to Limb(j)
    return T
"""

def get_data(filename):
    with open(filename, 'r') as infile:
        dataset = infile.read()
        n_rows = dataset[0:2]
        dataset = dataset[2:]
        dataset = dataset.strip().split('\t')
        # print(n_rows)
        # print(dataset)
        table = []
    for row in dataset:
        # split on tabs (or on any whitespace if you prefer row.split())
        fields = row.split('\t')
        # convert to int (or float) as needed:
        # numbers = [float(f) for f in fields]
        table.append(numbers)
        print(table)
    return table



def NeighborJoining(D):
    pass
    # print(D)


D = get_data('Neighbor_dataset.txt')
answer = NeighborJoining(D)
# print(answer)




