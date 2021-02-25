import sys
from collections import defaultdict
input=sys.stdin.readline
D,I,S,V,F=map(int,input().split())
g={}
street={}
for i in range(S):
    a,b,c,d=map(str,input().split())
    if int(b) not in g:
        g[b]=set()
    g[b].add(int(a))
    street[(a,b)]=(c,d)
cars=[]
for i in range(V):
    a,*b = input().split()
    cars.append(b)
print(len(g))

for nodes in g.keys():
    print(nodes)
    print(len(g[nodes]))
    for fromwhere in g[nodes]:
        print(street[(fromwhere,nodes)][0],'1')


