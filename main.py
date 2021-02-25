from collections import defaultdict, Counter

#TODO: What to do with the weight


graph = defaultdict(lambda: {'in': set(), 'out':set()})
d, i, s, v, f = map(int, input().split())

weight = defaultdict(int)

for i in range(s):
    a, b, name, wt = input().split()
    graph[a]['out'].add(name)
    graph[b]['in'].add(name)
    weight[name] = wt


cars_count = defaultdict(int)
for i in range(v):
    n, *roads = input().split()
    path_duration = 0
    for road in roads: 
        path_duration += weight[road]
    if path_duration <= d:
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
        mini = 10**9
        for r_ in graph[node]['in']:
            if cars_count[r_]:
                ct += 1
                mini = min(mini, cars_count[r_])
                road.append((r_, cars_count[r_]))
        temp['count'] = ct
        temp['roads'] = list(map(lambda x: (x[0], x[1]//mini), road))
        if len(road): ans.append(temp)


print(len(ans))
for i in ans:
    print(i['id'])
    print(i['count'])
    for road, dur in i['roads']: print(road, dur)

