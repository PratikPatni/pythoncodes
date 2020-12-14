t=int(input())
for i in range (t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    oc=0
    c=0
    for i in range(n):
        if l[i]%2!=0:oc+=1
    for i in range(n):
        if(l[i]%2==0):c+=oc
        else:oc-=1
    print(c)
