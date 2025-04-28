n = int(input())
a = [int(ai)-1 for ai in input().split(" ")]

position = 0
distances = dict()
distances[position] = 0

def find_closest(next: dict, distances: dict):
    imin, min = None, None
    for i in next:
        if imin is None or min is None:
            imin, min = i, distances[i]
        elif distances[i] < min:
            imin, min = i, distances[i]
    return imin


next = dict()
next[position+1] = position
distances[position+1] = distances[position]+1
if a[position] not in distances:
    next[a[position]] = position
    distances[a[position]] = distances[position]+1



while len(next) != 0:
    position = find_closest(next, distances)
    frompos = next.pop(position)
    if position+1 < n and position+1 not in next and position+1 not in distances:
        next[position+1] = position
        distances[position+1] = distances[position]+1
    if position-1 > 0 and position-1 not in next and position-1 not in distances:
        next[position-1] = position
        distances[position-1] = distances[position]+1
    if a[position] not in next and a[position] not in distances:
        next[a[position]] = position
        distances[a[position]] = distances[position]+1

for i in range(n):
    print(distances[i], end=" ")
