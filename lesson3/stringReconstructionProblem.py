import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.
def get_graph(kmers):
    edges_dict = {}
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix not in edges_dict:
            edges_dict[prefix]=[suffix]
        else:
            edges_dict[prefix].append(suffix)

    return edges_dict
# Insert your de_bruijn_string function here, along with any subroutines you need
def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string."""
    kmers = []
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        kmers.append(kmer)
    kmers.sort()

    return get_graph(kmers)

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
    start = max(out_minus_in, key=out_minus_in.get)
    end = min(out_minus_in, key=out_minus_in.get)
    return [start,end]


def eul_rec(node, not_visited, path):
    while node in not_visited.keys() and len(not_visited[node]) > 0:
        next_node = not_visited[node].pop()
        eul_rec(next_node, not_visited, path)
    path.append(node)
    return path[::-1]

def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian path in a graph."""
    not_visited = g
    path = []
    start_node = find_start_end(not_visited)[0]
    path = eul_rec(start_node, not_visited, path)

    return path

def genome_path(path: List[str]) -> str:
    """Forms the genome path formed by a collection of patterns."""
    answer = ""
    start = path[0]
    answer+=start
    for i in range(1,len(path)):
        next_nuc = path[i][-1]
        answer+=next_nuc
    return answer

# Insert your string_reconstruction function here, along with any subroutines you need
def string_reconstruction(patterns: List[str], k: int) -> str:
    """Reconstructs a string from its k-mer composition."""
    dB = get_graph(patterns)
    path = eulerian_path(dB) #build this
    Text = genome_path(path) #build this
    return Text