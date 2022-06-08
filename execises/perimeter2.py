import math

p1 = (-1,3)
p2 = (-1,-1)
p3 = (4,-1)
p4 = (1,3)
p_array = [p1, p2, p3, p4]
totalPerim = 0

def findDistanceAdd(pA, pB, totalPerim):
    x1, y1 = pA
    x2, y2 = pB
    gap_x = x2 - x1
    gap_y = y2 - y1
    currDist = math.sqrt(gap_x**2 + gap_y**2)
    totalPerim += currDist
    return totalPerim

for p in range(len(p_array)):
    try:
        totalPerim = findDistanceAdd(p_array[p], p_array[p+1], totalPerim)
    except IndexError:
        totalPerim = findDistanceAdd(p_array[p], p_array[0], totalPerim)

print(f'{totalPerim} is my answer')