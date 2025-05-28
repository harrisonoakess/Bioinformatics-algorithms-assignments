def burrows_wheeler_transform(text: str) -> str:
    """
    Generate the Burrows-Wheeler Transform of the given text.
    """

    list_of_BWT = []
    for i in range(len(text)):
       reverse_i = len(text)-i
       new_BWT = text[reverse_i:] + text[:reverse_i]
       list_of_BWT.append(new_BWT)
       list_of_BWT.sort()
    # print(list_of_BWT)
    return_string = ""
    for i in range(len(text)):
        return_string += list_of_BWT[i][len(text)-1]

    return return_string


text = "GCGTGCCTGGTCA$"
print(burrows_wheeler_transform(text))