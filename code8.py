t=int(input())
for i in range (t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    l.sort(reverse=True)
    if(n==1):print("first")
    elif(n==2):
        if(l[0]>l[1]):print("first")
        else:print("second")
    else:
        p1=l[0]
        p2=l[1]+l[2]
        for i in l[3:]:
          if i%2==1:p1=p1+i
          else:p2=p2+i
        if(p1==p2):print("draw")
        elif(p1>p2):print("first")
        else:print("second")
