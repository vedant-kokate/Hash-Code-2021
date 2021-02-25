from collections import defaultdict, Counter
from math import ceil

#TODO: What to do with the weight
def formula(wt, mini_wt, ct, mini_ct):
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


def formula1(curr_wt, sum_wt, mini_wt, mini_ct, cars_count, curr_car):
    temp = min(
            ceil((1 - curr_wt/sum_wt)* curr_car), 
            ceil(
                (mini_wt/curr_wt)*
                (cars_count/mini_ct)
            )
        )

    return min(
            d, 
            max(
                1, 
                temp
            )
        )


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
                road.append((r_, weight[r_]))
        temp['count'] = ct
        roads_processed = []
        s = 0
        for name, curr_wt in road:
            t = formula1(curr_car=cars_count[name] ,cars_count=cars_count[name], mini_wt=mini_wt, mini_ct=mini_cars ,curr_wt=curr_wt, sum_wt=sum(map(lambda x: weight[x], graph[node]['in'])))
            s += t
            roads_processed.append((name, t))
        
        temp['roads'] = list(map(lambda x: (x[0], ceil(x[1]/s * )), roads_processed))

        if len(road): ans.append(temp)


print(len(ans))
for i in ans:
    print(i['id'])
    print(i['count'])
    for road, dur in i['roads']: print(road, dur)

