dp=[0,1]
for i in range(2,60)://fibonacci %10 or -10  sequence repeats after 60 digits
    dp.append((dp[i-1]+dp[i-2])%10)//directly calc modulas as starting numbers have no role in last digit
for i in range(int(input())):
    n=int(input())
    c=0
    while(n>1):
        c+=1
        n=n//2
    print(dp[(2**c)%60-1])//first digit is 0
