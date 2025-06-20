file_name = "viterbiDataset.txt"
outcome_path = ""
outcomes = []
state_path = ""
states = []
probability_matrix = {}
transition_matrix = {}


with open(file_name) as in_file:
    lines = in_file.readlines()

    outcome_path = lines[0].strip()
    outcomes = lines[2].strip().split()
    states = lines[4].strip().split()

    i = 7
    for state1 in states:
        line = lines[i].strip().split()
        per_state_dict = {}
        j = 1
        for state2 in states:
            per_state_dict[state2] = float(line[j])
            j += 1
        transition_matrix[state1] = per_state_dict
        i += 1

    i = 11
    for state in states:
        line = lines[i].strip().split()
        per_state_dict = {}
        j = 1
        for outcome in outcomes:
            per_state_dict[outcome] = float(line[j])
            j += 1
        probability_matrix[state] = per_state_dict
        i += 1


backtrack = [{}]
probabilities = [{}]

for state in states:
    probabilities[0][state] = (1/len(states)) * probability_matrix[state][outcome_path[0]]
    backtrack[0][state] = None

for i in range(1,len(outcome_path)):
    outcome = outcome_path[i]
    probabilities.append({})
    backtrack.append({})
    for j in range(len(states)):
        state = states[j]
        max_prob = -1
        prev_st = None
        for prev_state in states:
            outcome_prob = probability_matrix[state][outcome]
            transition_prob = transition_matrix[prev_state][state]
            probability = probabilities[i-1][prev_state] * transition_prob * outcome_prob
            if probability > max_prob:
                max_prob = probability
                prev_st = prev_state
        probabilities[i][state] = max_prob
        backtrack[i][state] = prev_st

last_probs = probabilities[-1]
max_final_state = max(last_probs, key=last_probs.get)
path = [max_final_state]
for i in range(len(backtrack)):
    next_state = backtrack[-1-i][path[-1]]
    path.append(next_state)
state_path = path[::-1]
if state_path[-1] is None:
    state_path = state_path[:-1]
if state_path[0] is None:
    state_path = state_path[1:]
state_path = ''.join(state_path)
print(state_path)