from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your bw_matching function here, along with any subroutines you need
def bw_matching(bwt: str, patterns: List[str]) -> List[int]:
    """
    Perform Burrows-Wheeler Matching for a set of patterns against the Burrows-Wheeler Transform of a text.
    """
    lexi_text = sorted(bwt)
    table = {}
    keys = ['A', 'T', 'C', 'G', '$']
    atcg_count_front = {k: 0 for k in keys}
    atcg_count_back  = {k: 0 for k in keys}
    for i, j in zip(lexi_text, bwt):
        atcg_count_front[i] +=1 
        atcg_count_back[j] +=1
        
        table[(i,atcg_count_front[i])] = (j,atcg_count_back[j])
    front = list(table.keys())
    back = list(table.values())

    return_list = []
    for pattern in patterns:
        reverse_pattern = pattern[::-1]
        location = []
        for i in front:
            if i[0] == reverse_pattern[0]:
                location.append(i)
        # At this point, location is a list of evey tuple of the starting letter
        front_list = location
        back_list = []
        for i in range(0, len(reverse_pattern)-1):
            if i > 0:
                front_list[:] = back_list
                back_list.clear()
            for key in table.keys():
                if key in location and not table[key][0] == reverse_pattern[i+1]:
                    location.remove(key)
                if key in location and table[key][0] == reverse_pattern[i+1]:
                    back_list.append(table[key])
        return_list.append(len(back_list))
    return return_list





    


bwt = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
print(bw_matching(bwt, patterns))