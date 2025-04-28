n = int(input())
a = [int(ai)-1 for ai in input().split(" ")]

position = 0
distances = dict()
distances[position] = 0

next = dict()
next[1] = position
if a[position] not in distances:
    next[a[position]] = position

while len(next) != 0:
    position, frompos = next.popitem()
    distances[position] = distances[frompos] + 1
    if position+1 < n and position+1 not in next and position+1 not in distances:
        next[position+1] = position
    if a[position] not in next and a[position] not in distances:
        next[a[position]] = position

for i in range(n):
    print(distances[i], end=" ")
