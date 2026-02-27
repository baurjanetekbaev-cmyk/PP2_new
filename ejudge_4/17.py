import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# перемещаем координаты так, чтобы центр круга в начале координат
x1 -= 0
y1 -= 0
x2 -= 0
y2 -= 0

dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r

D = b*b - 4*a*c

if D <= 0:  
    t1 = t2 = -b/(2*a)
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD)/(2*a)
    t2 = (-b + sqrtD)/(2*a)

t_low = max(0, min(t1, t2))
t_high = min(1, max(t1, t2))

length = max(0, t_high - t_low) * math.sqrt(a)

print(f"{length:.10f}")