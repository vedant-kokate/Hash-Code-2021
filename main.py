from collections import defaultdict, Counter

#TODO: What to do with the weight
def formula(wt, mini_wt, ct, mini_ct):
    from math import ceil
    return max(ceil((mini_wt/wt)*(ct/mini_ct)), 1)


graph = defaultdict(lambda: {'in': set(), 'out':set()})
d, i, s, v, f = map(int, input().split())

weight = defaultdict(int)

for i in range(s):
    a, b, name, wt = input().split()
    graph[a]['out'].add(name)
    graph[b]['in'].add(name)
    weight[name] = int(wt)


cars_count = defaultdict(int)
for i in range(v):
    n, *roads = input().split()
    path_duration = 0
    for road in roads: 
        path_duration += int(weight[road])
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
        mini_cars = 10**9
        mini_wt = 10**9
        for r_ in graph[node]['in']:
            if cars_count[r_]:
                ct += 1
                mini_cars = min(mini_cars, cars_count[r_])
                mini_wt = min(mini_wt, weight[r_])
                road.append((r_, cars_count[r_]))
        temp['count'] = ct
        roads_processed = []
        for name, car_count in road:
            roads_processed.append((name, formula(weight[name], mini_wt, cars_count[name], mini_cars)))
        temp['roads'] = roads_processed

        if len(road): ans.append(temp)


print(len(ans))
for i in ans:
    print(i['id'])
    print(i['count'])
    for road, dur in i['roads']: print(road, dur)

