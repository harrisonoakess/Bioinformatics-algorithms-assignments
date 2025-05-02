"""
Solve the Frequent Words with Mismatches Problem ​

Input: A string Text as well as integers k and d (You may assume k<=12 and d<=3.)

Output: All most frequent k-mers with up to d mismatches in Text

Example input and output data are available in Cogniterra section 1.8. To get credit, you will have to submit this problem in two locations.
First, when you have working code, submit your solution in Cogniterra section 1.8. To get credit, it must pass the test in Cogniterra. 
Second, submit and upload your code here in Canvas.
"""

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

    """
    Pseudcode for frequent_words:

    FrequentWordsWithMismatches(Text, k, d)
    Patterns ← an array of strings of length 0
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n - k
        Pattern ← Text(i, k)
        neighborhood ← Neighbors(Pattern, d)
        for j ← 0 to |neighborhood| - 1
            neighbor ← neighborhood[j]
            if freqMap[neighbor] doesn't exist
                freqMap[neighbor] ← 1
            else
                freqMap[neighbor] ← freqMap[neighbor] + 1
    m ← MaxMap(freqMap)
    for every key Pattern in freqMap
        if freqMap[Pattern] = m
            append Pattern to Patterns
    return Patterns

    """


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

sample = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
print(frequent_words_with_mismatches(sample, k, d))