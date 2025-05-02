"""
Solve the Neighbors Problem ​

Input: A string Pattern and an integer d

Output: The collection of strings Neighbors(Pattern, d)

Example input and output data are available in Cogniterra section 1.11. To get credit, you will have to submit this problem in two locations. 
First, when you have working code, submit your solution in Cogniterra section 1.11. To get credit, it must pass the test in Cogniterra. 
Second, submit and upload your code here in Canvas.
"""
"""
Pseudocode for neighbors:

ImmediateNeighbors(Pattern)
    Neighborhood ← the set consisting of single string Pattern
    for i = 1 to |Pattern|
        symbol ← i-th nucleotide of Pattern
        for each nucleotide x different from symbol
            Neighbor ← Pattern with the i-th nucleotide substituted by x
            add Neighbor to Neighborhood
    return Neighborhood

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

s = "ACG"
d = 1
print(neighbors(s, d))