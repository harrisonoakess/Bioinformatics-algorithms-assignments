from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your better_bw_matching function here, along with any subroutines you need
def better_bw_matching(bwt: str, patterns: List[str]) -> List[int]:
    """
    Perform an optimized Burrows-Wheeler Matching for a set of patterns against the Burrows-Wheeler Transform of a text.
    """
    sorted_bwt = list(bwt)
    sorted_bwt.sort()
    front = ''.join(sorted_bwt)
    counts = [{'$':0, 'A':0, 'C':0, 'G':0, 'T':0}]
    first_occurance = {'$':0}
    for i in range(1,len(front) + 1):
        counts_map = counts[i-1].copy()
        b_char = bwt[i-1]
        if i < len(front):
            f_char = front[i]
            if f_char not in first_occurance:
                first_occurance[f_char] = i
        counts_map[b_char] += 1
        counts.append(counts_map)

    return_list = []
    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1
        while top <= bottom:
            if pattern:
                char = pattern[-1]
                pattern = pattern[:-1]
                if char in bwt[top:bottom + 1]:
                    top = first_occurance[char] + counts[top][char]
                    bottom = first_occurance[char] + counts[bottom + 1][char] - 1
                else:
                    return_list.append(0)
                    break
            else:
                return_list.append(bottom - top + 1)
                break
    return return_list

text = "GGCGCCGC$TAGTCACACACGCCGTA"
patterns = ["ACC", "CCG", "CAG"]
print(better_bw_matching(text, patterns))