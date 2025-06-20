file_name = "HMMdatasetPsuedo.txt"
threshold = 0
pseudocount = 1
alphabet = None
alignment = []

with open(file_name) as in_file:
    lines = in_file.readlines()

    threshold = lines[0].strip().split()[0]
    threshold = float(threshold)
    pseudocount = lines[0].strip().split()[1]
    pseudocount = float(pseudocount)
    alphabet = lines[2].strip().split()

    alignment_lines = lines[4:]
    for line in alignment_lines:
        line = line.strip()
        line = list(line)
        alignment.append(line)

alignment_star = []
alignment_star_indicies = []
for line in alignment:
    alignment_star.append([])
for i in range(len(alignment[0])):
    empty_count = 0
    for line in alignment:
        if line[i] == '-':
            empty_count += 1
    ratio = empty_count / len(alignment)
    if ratio < threshold:
        alignment_star_indicies.append(i)
        for j in range(len(alignment)):
            alignment_star[j].append(alignment[j][i])
            

# print(pseudocount)
# print(threshold)
# print(alphabet)
# print(alignment)
# print(alignment_star)

graph = {"S": [{"I0": 0}, {"D1": 0}, {"M1": 0}]}
graph["I0"] = [{"I0": 0}, {"D1": 0}, {"M1": 0}, ]
alphabet_dictionaries = {item: 0 for item in alphabet}
emissions = {"I0": alphabet_dictionaries}
for i in range(1,len(alignment_star[0])+1):
    I = "I" + str(i)
    M = "M" + str(i)
    M_next = "M" + str(i+1)
    D = "D" + str(i)
    D_next = "D" + str(i+1)

    emissions[I] = {item: 0 for item in alphabet}
    emissions[M] = {item: 0 for item in alphabet}

    if i != len(alignment_star[0]):
        graph[I] = [{I: 0}, {M_next: 0}, {D_next: 0}]
        graph[M] = [{I: 0}, {M_next: 0}, {D_next: 0}]
        graph[D] = [{I: 0}, {M_next: 0}, {D_next: 0}]
    else:
        graph[I] = [{I: 0}, {"E": 0}]
        graph[M] = [{I: 0}, {"E": 0}]
        graph[D] = [{I: 0}, {"E": 0}]

# print(graph)
# print(emissions)

for seq in alignment:
    prev_state = "S"
    match_index = 0
    for i, symbol in enumerate(seq):
        if i in alignment_star_indicies:
            match_index += 1
            if symbol == '-':
                curr_state = "D" + str(match_index)
            else:
                curr_state = "M" + str(match_index)
                emissions[curr_state][symbol] +=1

        else:
            if symbol == '-':
                continue
            curr_state = "I" + str(match_index)
            emissions[curr_state][symbol] +=1
        for d in graph[prev_state]:
            if curr_state in d:
                d[curr_state] += 1
        prev_state = curr_state
    for d in graph[prev_state]:
        if "E" in d:
            d["E"] += 1



states_order = ["S"]
num_match = len(alignment_star[0])
for i in range(0, num_match + 1):
    states_order.append(f"I{i}")
    if i < num_match:
        states_order.append(f"M{i+1}")
        states_order.append(f"D{i+1}")
states_order.append("E")

print('\t' + '\t'.join(states_order))
for from_state in states_order:
    row = [from_state]
    allowed = {}
    for d in graph.get(from_state, []):
        for key, value in d.items():
            allowed[key] = value
    total_counts = sum(allowed.values())
    raw_probs = {}
    for to_state in allowed:
        count = allowed[to_state]
        raw_probs[to_state] = count / total_counts if total_counts > 0 else 0
    for to_state in raw_probs:
        raw_probs[to_state] += pseudocount
    norm = sum(raw_probs.values())
    for to_state in states_order:
        if to_state in raw_probs:
            prob = raw_probs[to_state] / norm if norm > 0 else 0
        else:
            prob = 0
        row.append(str(round(prob, 3)))
    print('\t'.join(row))

print("--------")

print('\t' + '\t'.join(alphabet))
for state in states_order:
    row = [state]
    if state in emissions:
        total_emissions = sum(emissions[state].values())
        raw_probs = {}
        for symbol in alphabet:
            count = emissions[state][symbol]
            raw_probs[symbol] = count / total_emissions if total_emissions > 0 else 0
        for symbol in raw_probs:
            raw_probs[symbol] += pseudocount
        norm = sum(raw_probs.values())
        for symbol in alphabet:
            prob = raw_probs[symbol] / norm if norm > 0 else 0
            row.append(str(round(prob, 3)))
    else:
        row += ['0'] * len(alphabet)
    print('\t'.join(row))