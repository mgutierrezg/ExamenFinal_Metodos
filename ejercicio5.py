# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 


def dx_dt(x,y):
    return 10*(y-x)
def dy_dt(x,y,z):
    return 28 * (x - y -(x*z))
def dz_dt(x,y,z):
    return -2.67 * ( z + (x * y))

t = 0
h = 0.001
x = 0.0
y = 0.0
z = 0.0
kx1 = []
ky1 = []
kz1 = []
kx2 = []
ky2 = []
kz2 = []
kx3 = []
ky3 = []
kz3 = []
kx4 = []
ky4 = []
kz4 = []

while(t<5.0):
    
    for i in range(100000):
        kx1.append(dx_dt(x, y))
        ky1.append(dy_dt(x,y,z))
        kz1.append(dz_dt(x,y,z))
    
        kx2.append(dx_dt(x + h/2, y + ky1[i] * h/2))
        ky2.append(dy_dt(x + h/2, y + ky1[i] * h/2, z + kz1[i] * h/2))
        kz2.append(dz_dt(x + h/2, y + ky1[i] * h/2, z + kz1[i]* h/2))

            
        kx3.append(dx_dt(x + h/2, y + ky2[i] * h/2))
        ky3.append(dy_dt(x + h/2, y + ky2[i] * h/2, z + kz2[i] * h/2))
        kz3.append(dz_dt(x + h/2, y + ky2[i] * h/2, z + kz2[i] * h/2))
 
        kx4.append(dx_dt(x + h, y + ky3[i] * h))
        ky4.append(dy_dt(x + h, y + ky3[i] * h, z + kz3[i] * h))
        kz4.append(dz_dt(x + h, y + ky3[i] * h, z + kz3[i]* h))
    
    t += h
    #x += (h/6.0) * (kx1 + 2*kx2 + 2*kx3 + kx4);
    #y += (h/6.0) * (ky1 + 2*ky2 + 2*ky3 + ky4);
    #z += (h/6.0) * (kz1 + 2*kz2 + 2*kz3 + kz4);


print (kx1)



