"""
Solve the Reverse Complement Problem ​

Input: A DNA string Pattern.

Output: Patternrc, the reverse complement of Pattern.

Example input and output data are available in Cogniterra section 1.3. To get credit, you will have to submit this problem in two locations. 
First, when you have working code, submit your solution in Cogniterra section 1.3. To get credit, it must pass the test in Cogniterra. 
Second, submit and upload your code here in Canvas.
"""

import sys

with open('reverseComplementDataset.txt', 'r') as infile:
    dataset = infile.read()
    # print(len(dataset))
    # print(dataset)

return_string = ""

for i in dataset:
    match i:
        case "A":
            return_string += "T"
        case "T":
            return_string += "A"
        case "C":
            return_string += "G"
        case "G":
            return_string += "C"
        case "\n":
            return_string += "\n"

flipped_return_string = return_string[::-1]
# print(len(flipped_return_string))
print(flipped_return_string)        