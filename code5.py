t=int(input())
for i in range(t):
  s=int(input())
  ls=list()
  ls2=list()
  ls=(input().split(' '))
  for j in ls:ls2.append(int(j))
  print(min(ls2)*(s-1))
