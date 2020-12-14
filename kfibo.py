n,k=map(int, input().split())
l=list()
for i in range(n):
    if i<k:l.append(1)
    else:
        l.append(sum(l[-5:])%1000000007)
        i+=1
print(l[-1])
