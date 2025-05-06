"""

"""



def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    """Implements the GibbsSampling algorithm for motif finding."""
    








dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", 
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
k = 8
t = 5
n = 100

print(gibbs_sampler(dna, k, t, n))
