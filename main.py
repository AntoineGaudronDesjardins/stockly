n = int(input())
a = [int(ai)-1 for ai in input().split(" ")]

position = 0
distances = dict()
distances[position] = 0


def ordered_insert(array: list, node: int, distances: dict):
    l = len(array)
    for i in range(l):
        if distances[array[l-1-i]] < distances[node]:
            array.insert(l-i, node)
            break
    else:
        array.insert(0, node)
    return array


next = []
next.append(position+1)
distances[position+1] = distances[position]+1
if a[position] not in distances:
    next.append(a[position])
    distances[a[position]] = distances[position]+1


while len(next) != 0:
    position = next.pop(0)
    if position+1 < n and position+1 not in distances:
        distances[position+1] = distances[position]+1
        next = ordered_insert(next, position+1, distances)
    if position-1 > 0 and position-1 not in distances:
        distances[position-1] = distances[position]+1
        next = ordered_insert(next, position-1, distances)
    if a[position] not in distances:
        distances[a[position]] = distances[position]+1
        next = ordered_insert(next, a[position], distances)

for i in range(n):
    print(distances[i], end=" ")
