from collections import defaultdict

#TODO: What to do with the weight


graph = defaultdict(lambda: {'in': set(), 'out':set()})
d, i, s, v, f = map(int, input().split())
for i in range(s):
    a, b, name, wt = input().split()
    graph[a]['out'].add(name)
    graph[b]['in'].add(name)


# NAIVE Solution
ans = []
for node in graph:
    if graph[node]['in']:
        ans.append({
            'id': node,
            'count': len(graph[node]['in']),
            #'duration': d//len(graph[node]['in'])
            'duration': 1
        })

print(len(ans))
for i in ans:
    print(i['id'])
    print(i['count'])
    for j in graph[i['id']]['in']: print(j, i['duration'])
