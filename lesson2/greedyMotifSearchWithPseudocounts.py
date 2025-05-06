import random

"""
GreedyMotifSearch(Dna, k, t)
    BestMotifs ← motif matrix formed by first k-mers in each string from Dna
    for each k-mer Motif in the first string from Dna
        Motif1 ← Motif
        for i = 2 to t
            form Profile from motifs Motif1, …, Motifi - 1
            Motifi ← Profile-most probable k-mer in the i-th string in Dna
        Motifs ← (Motif1, …, Motift)
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

def profile_most_probable_kmer(text: str, k: int, profile: list[dict[str, float]]) -> str:
    stat_map = {}
    for i in range(len(text) - k + 1):
        potential_kmer = text[i:i + k]
        test_probability = 1
        for j in range(k):
            test_probability *= profile[j][potential_kmer[j]]
        stat_map[potential_kmer] = test_probability
    return max(stat_map, key=stat_map.get)

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
    return score

def greedy_motif_search_pseudocounts(dna: list[str], k: int, t: int) -> list[str]:
    best_motifs = []
    for seq in dna:
        best_motifs.append(seq[:k])
    for i in range(len(dna[0])-k+1):
        current_motifs = [dna[0][i:i+k]]
        for j in range(1,t):
            profile = form_profile(current_motifs)
            current_motifs.append(profile_most_probable_kmer(dna[j], k, profile))
        if get_score(current_motifs) < get_score(best_motifs):
            best_motifs = current_motifs
            
    return best_motifs 


input = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
k = 3
t = 5

print(greedy_motif_search_pseudocounts(input, k, t))