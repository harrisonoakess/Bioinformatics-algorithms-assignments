def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    return_string = ""

    for i in pattern:
        match i:
            case "A":
                return_string += "T"
            case "T":
                return_string += "A"
            case "C":
                return_string += "G"
            case "G":
                return_string += "C"
            case "\n":
                return_string += "\n"

    flipped_return_string = return_string[::-1]
    # print(len(flipped_return_string))
    # print(flipped_return_string) 
    return flipped_return_string

def hammingDistance(suf, text):
    count = 0
    for ch1, ch2 in zip(suf, text):
        if ch1 != ch2:
            count += 1
    return count

def neighbors(s: str, d: int) -> list[str]:
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A', 'C', 'G', 'T']
    return_list = []
    neighborhood = set()
    SuffixNeighbors = neighbors(s[1:], d)
    for text in SuffixNeighbors:
        if hammingDistance(s[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                neighborhood.add(x + text)
        else:
            neighborhood.add(s[0] + text)
    return list(neighborhood)

def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(0, n-k+1, 1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
        # add to dict
        for j in neighborhood:
            if j not in freqMap:
                freqMap[j] = 1
            else:
                freqMap[j] = freqMap[j] + 1
    m = max(freqMap.values())
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns

def frequent_words_mismatches_reverse_complements(text: str, k: int, d: int) -> list[str]:
    text2 = reverse_complement(text)
    texts = [text, text2]
    patterns = []
    freqMap = {}
    n = len(text)
    for t in texts:
        for i in range(0, n-k+1, 1):
            pattern = t[i:i+k]
            neighborhood = neighbors(pattern, d)
            # add to dict
            for j in neighborhood:
                if j not in freqMap:
                    freqMap[j] = 1
                else:
                    freqMap[j] = freqMap[j] + 1
    m = max(freqMap.values())
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1    

print(frequent_words_mismatches_reverse_complements(text, k, d))
