from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your inverse_burrows_wheeler_transform function here, along with any subroutines you need
def inverse_burrows_wheeler_transform(transform: str) -> str:
    """
    Generate the inverse of the Burrows-Wheeler Transform.
    """
    lexi_text = sorted(transform)
    table = {}
    keys = ['A', 'T', 'C', 'G', '$']
    atcg_count_front = {k: 0 for k in keys}
    atcg_count_back  = {k: 0 for k in keys}
    for i, j in zip(lexi_text, transform):
        atcg_count_front[i] +=1 
        atcg_count_back[j] +=1
        
        table[(i,atcg_count_front[i])] = (j,atcg_count_back[j])

    
    return_string = ""
    front = list(table.keys())
    back = list(table.values())
    return_string += front[0][0]
    next_iter = table[front[0]]
    return_string += next_iter[0]
    # print(return_string)
    for i in range(len(transform)-2):
        next_iter_int = front.index(next_iter)
        return_string += back[next_iter_int][0]
        next_iter = table[front[next_iter_int]]
    
    return_string = return_string[::-1]
    return return_string



text = "TTCCTAACG$A"
print(inverse_burrows_wheeler_transform(text))