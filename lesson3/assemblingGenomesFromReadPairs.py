import sys
from typing import List, Dict, Iterable, Tuple
import random
import copy

def get_graph(kmers):
    edges_dict = {}
    for kmer_tuple in kmers:
        kmer1 = kmer_tuple[0]
        kmer2 = kmer_tuple[1]
        prefixes = (kmer1[:-1], kmer2[:-1])
        suffixes = (kmer1[1:], kmer2[1:])
        if prefixes not in edges_dict:
            edges_dict[prefixes]=[suffixes]
        else:
            edges_dict[prefixes].append(suffixes)

    return edges_dict

def find_start_end(g: Dict[int, List[int]]) -> list[int]:
    out_minus_in = {}
    for node in g:
        edges = g[node]
        if node not in out_minus_in:
            out_minus_in[node] = len(edges)
        else:
            out_minus_in[node] += len(edges)
        for edge in edges:
            if edge not in out_minus_in:
                out_minus_in[edge] = -1
            else:
                out_minus_in[edge] -= 1

    if all(value == 0 for value in out_minus_in.values()):
        start = max(out_minus_in.keys())
        end = min(out_minus_in.keys())  
    else:
        start = max(out_minus_in, key=out_minus_in.get)
        end = min(out_minus_in, key=out_minus_in.get)
    
    return [start, end]



def eul_rec(node, not_visited, path):
    nodes_traveled = [node]
    path = []

    while nodes_traveled:
        current = nodes_traveled[-1]
        if current in not_visited and not_visited[current]:
            random.shuffle(not_visited[current])
            next_node = not_visited[current].pop()
            nodes_traveled.append(next_node)
        else:
            path.append(nodes_traveled.pop())
    
    return path[::-1]


def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]:
    not_visited = copy.deepcopy(g)
    path = []
    start_node = find_start_end(not_visited)[0]
    path = eul_rec(start_node, not_visited, path)

    return path

def genome_path(path: List[Tuple[str,str]], n: int, k, d) -> str:
    """Forms the genome path formed by a collection of patterns."""
    string1 = path[0][0]
    string2 = path[0][1]

    for i in range(1, len(path)):
        string1 += path[i][0][-1]
        string2 += path[i][1][-1]

    return string1 + string2[-(k + d):]

def StringReconstructionReadPairs(PairedReads: List[Tuple[str, str]], k: int, d: int) -> str:
    dB = get_graph(PairedReads)
    n = k + d
    is_right_path = False
    path = []
    z = 0
    while not is_right_path:
        is_right_path = True
        path = eulerian_path(dB)
        for i in range(len(path) - n):
            if path[n + i][0][:(k-1)] != path[i][1][:(k-1)]:
                is_right_path = False
                break
        if z == 5:
            is_right_path = True
        z+=1

    Text = genome_path(path, n, k, d) 
    return Text

# PairedReads = [
#     ("GTTT", "ATTT"),
#     ("TTTA", "TTTG"),
#     ("TTAC", "TTGT"),
#     ("TACG", "TGTA"),
#     ("ACGT", "GTAT"),
#     ("CGTT", "TATT")
# ]

# PairedReads = [
#     ("ACAC", "CTCT"),
#     ("ACAT", "CTCA"),
#     ("CACA", "TCTC"),
#     ("GACA", "TCTC")
# ]

# PairedReads = [
#     ("GGG", "GGG"),
#     ("AGG", "GGG"),
#     ("GGG", "GGT"),
#     ("GGG", "GGG"),
#     ("GGG", "GGG")
# ]

PairedReads = [
    ("AAG", "CTT"),
    ("ACA", "GCC"),
    ("AGA", "TTT"),
    ("AGC", "TTT"),
    ("AGT", "TAC"),
    ("CAA", "CCT"),
    ("GAG", "TTA"),
    ("GTT", "ACA"),
    ("TAC", "AGC"),
    ("TTA", "AAG"),
    ("TTT", "CAA")

]


k = 4
d = 2

print(StringReconstructionReadPairs(PairedReads, k, d))