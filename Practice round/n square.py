import time
st=time.time()
f=open("/home/vedant/program files/Hash-Code-2021/Practice round/input/c_many_ingredients", "r")
out=open("/home/vedant/program files/Hash-Code-2021/Practice round/output/c_many_ingredients", "w")
M,T2,T3,T4=map(int,f.readline().split())

p={}
pizza=[]
for i in range(M):
    p[i]=set()
    x=f.readline().split()
    pizza.append([x[0],i])
    for j in range(1,len(x)):
        p[i].add(x[j])
pizza.sort(reverse=True)

###########For 2's pair
ans=[]
for i in range(M-1):
    ans.append([i,i+1,0])
    pi=p[pizza[i][1]]
    for j in range(i+1,M):
        
        pj=p[pizza[j][1]]
        if len(pi)+len(pj)<ans[-1][-1]:
            break
        tempadd=len(pi.union(pj))
        if tempadd>ans[-1][-1]:
            ans[-1]=[i,j,tempadd]
print("1/6")
print(time.time()-st,'s')
ans.sort(reverse=True ,key=lambda x:x[2])
used=[False]*M


cur=0
while T2>0:
    if used[ans[cur][0]] or used[ans[cur][1]]:
        cur+=1
        continue
    out.write("2 "+str(ans[cur][0])+" "+str(ans[cur][1])+"\n")
    used[ans[cur][0]]=True
    used[ans[cur][1]]=True
    cur+=1
    T2-=1
print("2/6")
print(time.time()-st,'s')

ans=[]
for i in range(M-1):
    if used[i]:
        continue
    ans.append([i,i+1,0])
    pi=p[pizza[i][1]]
    for j in range(i+1,M):
        if used[j]:
            continue
        pj=p[pizza[j][1]]
        if len(pi)+len(pj)<ans[-1][-1]:
            break
        tempadd=len(pi.union(pj))
        if tempadd>ans[-1][-1]:
            ans[-1]=[i,j,tempadd]
print("3/6")
print(time.time()-st,'s')

for i in range(len(ans)):
    if i*100/len(ans)==i*100//len(ans):
        print(i*100/len(ans),'%')
    ans[i].insert(2,0)
    for j in range(M):
        if used[j]:
            continue
        tempadd=len(p[ans[i][0]].union(p[ans[i][1]].union(p[j])))
        if tempadd>ans[i][3]:
            ans[i][2]=j
            ans[i][3]=tempadd
    print("out")
ans.sort(reverse=True,key=lambda x:x[3])
print("4/6")
print(time.time()-st,'s')
cur=0
while T3>0 and cur<len(ans):
    
    if used[ans[i][0]] or used[ans[i][1]] or used[ans[i][2]]:
        cur+=1
        continue
    out.write("3 "+str(ans[cur][0])+" "+str(ans[cur][1])+" "+str(ans[cur][2])+"\n")
    used[ans[cur][0]]=True
    used[ans[cur][1]]=True
    used[ans[cur][2]]=True
    cur+=1
print("5/6")
print(time.time()-st,'s')



