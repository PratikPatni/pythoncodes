n=int(input())
output=list()
for i in range(n):
    s=int(input())
    ls=list()
    ls=input().split(' ')
    ls2=ls
    ls.reverse()
    if(ls2==ls):output.append("yes")
    else:output.append("no")
for i in range(output):print(i)
