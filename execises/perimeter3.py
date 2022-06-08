import math

p1 = (-1,3)
p2 = (-1,-1)
p3 = (4,-1)
p4 = (1,3)
p_array = [p1, p2, p3, p4]

totalPerim = 0
prevPt = p4
for p in p_array:
    x1, y1 = prevPt
    x2, y2 = p
    currDist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    totalPerim += currDist
    prevPt = p

print(f'{totalPerim} is my answer')