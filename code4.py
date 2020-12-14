#sorting numbers discarding repititon
t=int(input())
for i in range(t):
    n=int(input())
    ls=list(map(int,input().strip().split()))
    ls2=list()
    s=set(ls)#converting to sets as sets automatically removes duplicataes
    ls=sorted(s)#converting to list sorted returns a list but wait the numbers are string so sort them again
    for i in ls:ls2.append(int(i))
    ls2=sorted(ls2)#finally sorted list
    for i in ls2:print(i)
