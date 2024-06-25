import numpy as np

i=np.array([1,0,0])
j=np.array([0,1,0])
k=np.array([0,0,1])

x1=int(input(" the x-component of the first vector:  "))
y1=int(input(" the y-component of the first vector:  "))
z1=int(input(" the z-component of the first vector:  "))
r1= x1*i + y1*j + z1*k

x2=int(input(" the x-component of the second vector:  "))
y2=int(input(" the y-component of the second vector:  "))
z2=int(input(" the z-component of the second vector:  "))
r2= x2*i + y2*j + z2*k

x=[x1,x2]
y=[y1,y2]
z=[z1,z2]

def scalar_product_cartesian(x,y,z):
    r=(x[0]*x[1]+y[0]*y[1]+z[0]*z[1])
    return r

spc= scalar_product_cartesian(x,y,z)

print("r1 = ", r1)
print("r2 = ", r2)
print("r1.r2 =", spc)