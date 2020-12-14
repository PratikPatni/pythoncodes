n=int(input())
for i in range(n):
    a=int(input())
    ls=list()
    ls=input().split(' ')
    freq = dict()
    for item in ls:
      if (item in freq):freq[item] += 1
      else:freq[item] = 1
    ma=0
    mode=int(max(freq.keys()))
    for j in freq:
        if(freq[j]>ma):
            ma=freq[j]
            mode=j
        elif(freq[j]==ma):
            ma=freq[j]
            mode=min(r,j)
    print(mode)
