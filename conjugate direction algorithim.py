import numpy as np
print("RegNo 2367413  Name:Nishant    Prog:Matrix Multiplication")

def g(q,x0,b):
    G=np.dot(q,x0)-b
    return G
def alpha(g,d,q):
    gt=np.transpose(g)
    dt=np.transpose(d)
    a=(np.dot(gt,d)/np.dot(np.dot(dt,q),d))*-1
    return a[0]
def xnext(x,a,d):
    d=d.reshape((2,1))
    xn=x+a*d
    return xn
def func(x,q,b):
    f=.5*(np.dot(np.dot(np.transpose(x),q),x))-np.dot(np.transpose(x),b)
    return f
def read_matrix(n,p):
    a=[]
    for i in range(n):
        b = []
        for j in range(p):
            b.append(int(input()))
        a.append(b)
    a=np.array(a)
    return a
n=int(input("enter q matrix size"))
q=read_matrix(n,n)
print("enter elements for starting point")
x=read_matrix(n,1)
print("enter elements for b matrix")
b=read_matrix(n,1)
print("enter elements for direction matrix")
d=read_matrix(n,n)
for i in range(n):
    g0=g(q,x,b)
    print("g",i,"=\n",g0)
    a=alpha(g0,d[i],q)
    print("alpha",i,"=",a)
    x=xnext(x,a,d[i])
    print("x",i+1,"=\n",x)
    print("function value at x",i+1,"=",func(x,q,b))
