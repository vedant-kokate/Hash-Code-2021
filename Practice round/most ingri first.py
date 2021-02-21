f=open("/home/vedant/program files/Hash-Code-2021/Practice round/input/a_example", "r")
out=open("/home/vedant/program files/Hash-Code-2021/Practice round/output/a_example", "w")
M,T2,T3,T4=map(int,f.readline().split())
pizza=[]
for i in range(M):
    x=f.readline().split()
    pizza.append([x[0],i])
pizza.sort(reverse=True)
totteam=0
##
i=0
while M>0 and (T2>0 or T3>0 or T4>0):
    if T2>0:
        T2-=1
        out.write("2 "+str(pizza[i][1])+" "+str(pizza[i+1][1])+"\n")
        i+=2
        M-=2
        continue
    if T3>0:
        if M-3<0:
            break
        T3-=1
        out.write("3 "+str(pizza[i][1])+" "+str(pizza[i+1][1])+" "+str(pizza[i+2][1])+"\n")
        i+=3
        M-=3
    if T4>0:
        if M-4<0:
            break
        T4-=1
        out.write("4 "+str(pizza[i][1])+" "+str(pizza[i+1][1])+" "+str(pizza[i+2][1])+" "+str(pizza[i+3][1])+"\n")
        i+=4
        M-=4



