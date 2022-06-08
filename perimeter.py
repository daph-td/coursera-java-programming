import math

def p(x, y):
    len_x = x
    len_y = y
    return len_x, len_y

def findDistance(pA, pB):
    x1, y1 = pA
    x2, y2 = pB
    gap_x = x2 - x1
    gap_y = y2 - y1
    return math.sqrt(gap_x**2 + gap_y**2)

p1 = p(-1,3)
p2 = p(-1,-1)
p3 = p(4,-1)
p4 = p(1,3)

d12 = findDistance(p1, p2)
d23 = findDistance(p2, p3)
d34 = findDistance(p3, p4)
d41 = findDistance(p4, p1)

per = d12 + d23 + d34 + d41
print(f'{per} is my answer')