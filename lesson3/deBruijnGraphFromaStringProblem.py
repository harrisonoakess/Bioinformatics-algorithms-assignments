def de_bruijn_string(text: str, k: int) -> dict[str, list[str]]:
    """Forms the de Bruijn graph of a string."""
    connections = {}
    for i in range(0, len(text)-k+1):
        key = text[i:i+k-1]
        # print(text[i])
        if key not in connections:
            connections[key] = []
        connections[key].append(text[i+1:i+k])

    sorted_connections = {}
    for key in sorted(connections):
        sorted_connections[key] = sorted(connections[key])
    return(sorted_connections)



text ="AGCCT"
k = 4

print(de_bruijn_string(text, k))