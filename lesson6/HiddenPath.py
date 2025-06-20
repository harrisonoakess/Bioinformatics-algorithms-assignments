import sys
import re

with open("HiddenPath1.txt", "r") as infile:
    lines = infile.readlines()


text = lines[0]
letters = lines[2]
letters = re.sub(r"\s+", "", letters)
print(len(letters))
table = lines[5:]
# print(letters)
# print(table)

numbers = []
for line in table:
    values = re.findall(r"\d+\.\d+", line)
    for i in values:
        i = float(i)
    numbers.append(values)
AtoA = float(numbers[0][0])
AtoB = float(numbers[0][1])
BtoA = float(numbers[1][0])
BtoB = float(numbers[1][1])

answer = 1/len(letters)
print(answer)




for i in range(len(text)-1):
    if text[i] == "A" and text[i+1] == "A":
        answer *= AtoA
    if text[i] == "A" and text[i+1] == "B":
        answer *= AtoB
    if text[i] == "B" and text[i+1] == "A":
        answer *= BtoA
    if text[i] == "B" and text[i+1] == "B":
        answer *= BtoB

print(answer)