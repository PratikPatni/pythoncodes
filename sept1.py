t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().strip().split()))
    s=set(ls)
    c=0
    for j in s:
        if int(j)!=0:c+=1
    print(2**c)
