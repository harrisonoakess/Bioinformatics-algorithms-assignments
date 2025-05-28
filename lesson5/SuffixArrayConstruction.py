import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your suffix_array function here, along with any subroutines you need
def suffix_array(text: str) -> List[int]:
    """
    Generate the suffix array for the given text.
    """
    list_of_tuples = []

    for i in range(len(text)):
        list_of_tuples.append((text[i:], i))
    list_of_tuples.sort()
    list_of_integers = []
    for text, iter in list_of_tuples:
        # print(iter)
        list_of_integers.append(iter)
    print(list_of_integers)
    # return list_of_integers


text = "AACGATAGCGGTAGA$"
print(suffix_array(text))