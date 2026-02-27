xA, yA = map(float, input().split())
xB, yB = map(float, input().split())

yB_reflected = -yB


if xB == xA:
    xR = xA
else:
    xR = xA + (0 - yA)*(xB - xA)/(yB_reflected - yA)

yR = 0.0

print(f"{xR:.10f} {yR:.10f}")