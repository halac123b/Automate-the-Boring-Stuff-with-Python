list1 = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

list2 = []

for i in range(len(list1[0])):
    subList = []
    for j in range(len(list1)):
        subList += [list1[j][i]]
    list2.append(subList)

print("[")
for i in range(len(list2)):
    print(list2[i], end='')
    print(",")
print("]")
# print(list2)