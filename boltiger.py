import math
for i in range(int(input())):
    finish,distancetoBolt,tigerAccelaration,boltSpeed=map(int,input().split())
    tb=finish/boltSpeed
    tt=math.sqrt(2*(distancetoBolt+finish)/tigerAccelaration)
    if tt>tb:print("Bolt")
    else:print("Tiger")
