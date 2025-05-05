def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
    best_probability = 0
    best_kmer = ''

    for i in range(0, len(text) - k +1):
        potential_kmer = text[i:i+k]
        test_probability = 1
        for j in range(k):
            test_probability *= profile[j][potential_kmer[j]]
        if test_probability > best_probability:
            best_probability = test_probability
            best_kmer = potential_kmer
    return best_kmer


#sample input 1
text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = [{"A": 0.2, "C": 0.4, "G": 0.3, "T": 0.1}, 
           {"A": 0.2, "C": 0.3, "G": 0.3, "T": 0.2},
           {"A": 0.3, "C": 0.1, "G": 0.5, "T": 0.1},
           {"A": 0.2, "C": 0.5, "G": 0.2, "T": 0.1},
           {"A": 0.3, "C": 0.1, "G": 0.4, "T": 0.2}]


print(profile_most_probable_kmer(text, k, profile))
