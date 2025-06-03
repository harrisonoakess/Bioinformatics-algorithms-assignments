import sys
from typing import List, Dict, Iterable, Tuple

def burrows_wheeler_transform(text: str) -> str:
    BWT_matrix = [text]
    transformed_text = ""

    for i in range(len(text) - 1):
        BWT_matrix.append(BWT_matrix[i][-1] + BWT_matrix[i][:-1])

    BWT_matrix.sort()

    for string in BWT_matrix:
        transformed_text += string[-1]
    return transformed_text

def make_suffix_array(text: str) -> List[int]:
    list_of_tuples = []

    for i in range(len(text)):
        list_of_tuples.append((text[i:], i))
    list_of_tuples.sort()
    list_of_integers = []
    for text, iter in list_of_tuples:
        list_of_integers.append(iter)
    return list_of_integers

def make_partial_suffix_array(text: str, k: int) -> List[int]:
    full_sa = make_suffix_array(text)
    partial = []
    for i in range(len(full_sa)):
        text_position = full_sa[i]
        if text_position % k == 0:
            partial.append((i, text_position))
    return partial
def multiple_pattern_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    return_dict = dict.fromkeys(patterns, [])
    k = 5
    text += '$'
    suffix_array = make_partial_suffix_array(text, k)
    bwt = burrows_wheeler_transform(text)
    sorted_bwt = list(bwt)
    sorted_bwt.sort()
    front = ''.join(sorted_bwt)
    alphabet = set(bwt)
    counts = [{ch: 0 for ch in alphabet}]
    first_occurance = {}
    for i in range(1,len(front) + 1):
        counts_map = counts[i-1].copy()
        b_char = bwt[i-1]
        if i < len(front):
            f_char = front[i]
            if f_char not in first_occurance:
                first_occurance[f_char] = i
        counts_map[b_char] += 1
        counts.append(counts_map)

    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1
        cut_pattern = pattern
        while top <= bottom:
            if cut_pattern:
                char = cut_pattern[-1]
                cut_pattern = cut_pattern[:-1]
                if char in bwt[top:bottom + 1]:
                    top = first_occurance[char] + counts[top][char]
                    bottom = first_occurance[char] + counts[bottom + 1][char] - 1
                else:
                    break
            else:
                matches = []
                for i in range(top, bottom + 1):
                    steps_back = 0
                    j = i
                    while j not in dict(suffix_array):
                        next_char = bwt[j]
                        j = first_occurance[next_char] + counts[j][next_char]
                        steps_back += 1
                    array_index = dict(suffix_array)[j]
                    index_match = array_index + steps_back
                    matches.append(index_match)
                return_dict[pattern] = matches
                break
    return return_dict


text = "AATCGGGTTCAATCGGGGT"
# text = "ATATATATAT"
# text = "bananas"
patterns = ["ATCG", "GGGT"]
# patterns = ["GT", "AGCT", "TAA", "AAT", "AATAT"]
# patterns = ["ana", "as"]
print(multiple_pattern_matching(text, patterns))