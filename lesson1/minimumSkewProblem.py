"""
Solve the Minimum Skew Problem ​

Input: A DNA string Genome

Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|)

Example input and output data are available in Cogniterra section 1.7. To get credit, you will
 have to submit this problem in two locations. First, when you have working code, submit your 
 solution in Cogniterra section 1.7. To get credit, it must pass the test in Cogniterra. 
 Second, submit and upload your code here in Canvas.
"""

# import sys

# with open('minimumSkewDataset.txt', 'r') as infile:
#     dataset = infile.read()
#     # print(len(dataset))
#     # print(dataset)

input_1 = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

counter = 0
return_list = []
lowest_value = 0
index = 0

for i in input_1:
    if i == "C":
        counter -= 1
    if i == "G":
        counter += 1
    if counter < lowest_value:
        return_list = []
        return_list.append(index + 1)
        lowest_value = counter
        index += 1
        continue
    if counter == lowest_value:
        return_list.append(index + 1)
    index += 1
print(return_list)


