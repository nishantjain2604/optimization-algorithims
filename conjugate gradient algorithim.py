print("RegNo 2367413  Name:Nishant    Prog:conjugate gradient algorithim")
import numpy as np
def g(q,x0,b):
    G=np.dot(q,x0)-b
    return G
def alpha(g,d,q):
    gt=np.transpose(g)
    dt=np.transpose(d)
    a=(np.dot(gt,d)/np.dot(np.dot(dt,q),d))*-1
    return a[0][0]
def xnext(x,a,d):
    d=d.reshape((n,1))
    xn=x+a*d
    return xn
def directon(g,q,d0):
    bk=np.dot(np.dot(np.transpose(g),q),d0)/np.dot(np.dot(np.transpose(d0),q),d0)
    dnext=-g+bk*d0
    return dnext
def read_matrix(n,p):
    a=[]
    for i in range(n):
        b = []
        for j in range(p):
            b.append(int(input()))
        a.append(b)
    a=np.array(a)
    return a
def func(x,q,b):
    f=.5*(np.dot(np.dot(np.transpose(x),q),x))-np.dot(np.transpose(x),b)
    return f[0][0]
n=int(input("enter q matrix size"))
q=read_matrix(n,n)
print("enter elements for starting point")
x=read_matrix(n,1)
print("enter elements for b matrix")
b=read_matrix(n,1)
#print("enter elements for direction matrix")
d=0
for i in range(n):
    g0=g(q,x,b)
    print("g",i,"=\n",g0)
    if i==0:
        d=-1*g0
        print("initial direction\n",d)
    else:
        d=directon(g0,q,d)
        print("next direction",d)
    a=alpha(g0,d,q)
    print("alpha",i,"=",a)
    x=xnext(x,a,d)
    print("x",i+1,"=\n",x)
    print("function value at x", i+1, "=", func(x, q, b))
