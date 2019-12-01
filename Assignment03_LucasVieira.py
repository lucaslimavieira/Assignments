import math

sides = int(input("Define the number of polygonon points:"))

n = sides
x = []
y = []

for n in range(n):
    coord_x = float(input(f"Define the x coordinate for the point {n+1} :"))
    coord_y = float(input(f"Define the y coordinate for the point {n+1} :"))
    x.append(coord_x)
    y.append(coord_y)

n = sides
print(f"\nPoints {'x':>5} {'y':>10}")
print("-" * 23)
for n in range(n):
    print(f"{n+1} {x[n]:10.2f} {y[n]:10.2f}")
 
ax=0
sx=0
sy=0
ix=0
iy=0
ixy=0
xt=0
yt=0
ixt=0
iyt=0
ixyt=0


print("\nGeometric characteristics")
print("-" * 25)

x.append(x[0])
y.append(y[0])
n = sides
print(x)
print(y)
print(n)
for i in range(n):
    ax = ((x[i+1]*y[i])-(y[i+1]*x[i])) + ax
ax = ax/2
if ax<0:
    ax=-ax
print(f"Ax={ax:9.2f}")

n = sides - 1
for i in range(n):
    sx = ((x[i+1] - x[i]) * (y[i+1]**2 + y[i]*y[i+1] + y[i]**2)) + sx
sx = sx/-6
print(f"Sx={sx:9.2f}")

n = sides - 1
for i in range(n):
    sy = ((y[i+1] - y[i]) * (x[i+1]**2 + x[i]*x[i+1] + x[i]**2)) + sy
sy = sy/6
print(f"Sy={sy:9.2f}")

n = sides - 1
for i in range(n):
    ix = ((x[i+1] - x[i]) * (y[i+1]**3 + (y[i+1]**2)*y[i] + y[i+1]*(y[i]**2) + y[i]**3)) + ix
ix = ix/-12
print(f"Ix={ix:9.2f}")

n = sides - 1
for i in range(n):
    iy = ((y[i+1] - y[i]) * (x[i+1]**3 + (x[i+1]**2)*x[i] + x[i+1]*(x[i]**2) + x[i]**3)) + iy
iy = iy/12
print(f"Iy={iy:9.2f}")

n = sides - 1
for i in range(n):
    ixy = ((y[i+1] - y[i]) * (y[i+1] * (3*x[i+1]**2 + 2*x[i+1]*x[i] + x[i]**2) + y[i] *(3*x[i]**2 + 2*x[i+1]*x[i] + x[i+1]**2))) + ixy
ixy = ixy/-24
print(f"Ixy={ixy:8.2f}")

print(f"Xt={sy/ax:9.2f}")
print(f"Yt={sx/ax:9.2f}")
print(f"Ixt={ix-(sx/ax)**2*ax:8.2f}")
print(f"Iyt={iy-(sy/ax)**2*ax:8.2f}")
print(f"Ixyt={ixy+(sy/ax)*(sx/ax)*ax:7.2f}")