import math

getAngle = int(input('How many angles does the shape have? '))

p_array = []
for angle in range(getAngle):
    xPt = int(input(f'Please input x of the angle {angle+1}: '))
    yPt = int(input(f'Please input y of the angle {angle+1}: '))
    getCoor = (xPt, yPt)
    p_array.append(getCoor)

print(p_array)
# p1 = (-1,3)
# p2 = (-1,-1)
# p3 = (4,-1)
# p4 = (1,3)
# p_array = [p1, p2, p3, p4]

totalPerim = 0
prevPt = p_array[-1]
for p in p_array:
    x1, y1 = prevPt
    x2, y2 = p
    totalPerim += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    prevPt = p

print(f'{totalPerim} is my answer')