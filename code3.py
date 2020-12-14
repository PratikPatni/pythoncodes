w,bal= map(float,input().split(' '))
if w%5==0.0:
    if w+0.5<=bal:
        bal=bal-w-0.5
print('%.2f'bal)
