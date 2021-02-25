from collections import defaultdict, Counter

#TODO: What to do with the weight


graph = defaultdict(lambda: {'in': set(), 'out':set()})
d, i, s, v, f = map(int, input().split())
for i in range(s):
    a, b, name, wt = input().split()
    graph[a]['out'].add(name)
    graph[b]['in'].add(name)

cars_count = defaultdict(int)
for i in range(v):
    n, *roads = input().split()
    for road in roads: cars_count[road] += 1


# NAIVE Solution
ans = []
for node in graph:
    if graph[node]['in']:
        temp = {
            'id': node,
        }
        ct = 0
        road = []
        for r_ in graph[node]['in']:
            if cars_count[r_]:
                ct += 1
                road.append((r_, cars_count[r_]))
        temp['count'] = ct
        temp['roads'] = road
        if len(road): ans.append(temp)


print(len(ans))
for i in ans:
    print(i['id'])
    print(i['count'])
    for road, dur in i['roads']: print(road, dur)
