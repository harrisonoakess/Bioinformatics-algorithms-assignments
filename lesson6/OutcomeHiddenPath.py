import sys
import re

with open("HiddenPath2.txt", "r") as infile:
    lines = infile.readlines()

text1 = lines[0]
text1 = text1.upper()
letters1 = lines[2]
letters1 = re.sub(r"\s+", "", letters1)
text2 = lines[4]
letters2 = lines[6]
letters2 = re.sub(r"\s+", "", letters2)
table = lines[9:]

numbers = []
for line in table:
    values = re.findall(r"\d+\.\d+", line)
    for i in values:
        i = float(i)
    numbers.append(values)
AtoX = float(numbers[0][0])
AtoY = float(numbers[0][1])
AtoZ = float(numbers[0][2])
BtoX = float(numbers[1][0])
BtoY = float(numbers[1][1])
BtoZ = float(numbers[1][2])

answer = 1
for i,j in zip(text1, text2):
    if i == "X" and j == "A":
        answer *= AtoX
    if i == "Y" and j == "A":
        answer *= AtoY
    if i == "Z" and j == "A":
        answer *= AtoZ
    if i == "X" and j == "B":
        answer *= BtoX
    if i == "Y" and j == "B":
        answer *= BtoY
    if i == "Z" and j == "B":
        answer *= BtoZ

print(answer)