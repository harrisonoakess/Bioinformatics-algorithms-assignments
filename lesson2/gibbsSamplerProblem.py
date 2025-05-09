import random

"""
GibbsSampler(Dna, k, t, N)
 randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
 BestMotifs ← Motifs
 for j ← 1 to N
     i ← Random(t)
     Profile ← profile matrix constructed from all strings in Motifs except for Motifi
     Motifi ← Profile-randomly generated k-mer in the i-th sequence
     if Score(Motifs) < Score(BestMotifs)
         BestMotifs ← Motifs
 return BestMotifs
"""

def form_profile(motif: list[str]):
    profile = []
    for i in range(len(motif[0])):
        positionDictionary = {'A':1,'C':1,'G':1,'T':1}
        for nuc in motif:
            positionDictionary[nuc[i]] +=1
        for nuc in positionDictionary:
            positionDictionary [nuc] /= len(motif) + 2
        profile.append(positionDictionary)
    # print(profile)
    return profile

def get_score(motifs: list[str]):
    score = 0
    for i in range(len(motifs[0])):
        positionDictionary = {'A':0,'C':0,'G':0,'T':0}
        for seq in motifs:
            # print(seq)
            # print(i)
            positionDictionary[seq[i]]+=1
        maxCount = max(positionDictionary.values())
        score += len(motifs)-maxCount
    print(score)
    return score

def profile_most_probable_kmer(text: str, k: int, profile: list[dict[str, float]]) -> str:
    weights = []
    kmers = []
    for i in range(len(text) - k + 1):
        potential_kmer = text[i:i + k]
        kmers.append(potential_kmer)
        test_probability = 1
        for j in range(k):
            test_probability *= profile[j][potential_kmer[j]]
        weights.append(test_probability)
    return random.choices(kmers, weights)[0]
        # stat_map[potential_kmer] = test_probability
    # print(stat_map)
    # return max(stat_map, key=stat_map.get)

def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    """Implements the GibbsSampling algorithm for motif finding."""
    best_motifs = []
    for i in dna:
        random_int = random.randint(0, len(i) - k)
        random_selection = i[random_int:random_int + k]
        best_motifs.append(random_selection)
    current_motifs = best_motifs
    for iter in range(0,n):
        remove_int = random.randint(0,t-1)
        removed_motif = current_motifs[remove_int]
        current_motifs.remove(removed_motif)
        removed_string = dna[remove_int]
        dna.remove(removed_string)
        profile = form_profile(current_motifs)
        current_motifs.append(profile_most_probable_kmer(removed_string, k, profile))
        dna.append(removed_string)
        if get_score(current_motifs) < get_score(best_motifs):
            best_motifs = current_motifs
    return best_motifs    
    








dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", 
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
k = 8
t = 5
n = 100

print(gibbs_sampler(dna, k, t, n))
