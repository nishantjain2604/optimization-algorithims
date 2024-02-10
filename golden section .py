print("RegNo 2367413  Name:Nishant    Prog:golden section algorithim")
import numpy as np
rho=(3-(5)**.5)/2
def function(x):
    result= x**4-14*(x**3)+60*(x**2)-70*x
    return result
range_ab=[0,2]
locate_x=.3
n=1
while (.61803**n)>=locate_x/2:
    n=n+1
print("No of iterations",n)
def ab(a0,b0):
    a_next=a0+rho*(b0-a0)
    b_next=a0+(1-rho)*(b0-a0)
    return a_next,b_next
for i in range(n):
    a,b=ab(range_ab[0],range_ab[1])
    f1=function(a)
    f2=function(b)
    print(f'f(a{i+1})= {f1},f(b{i+1})= {f2}')
    new=max(f1,f2)
    print("\nmax=",new)
    if new==f1:
        range_ab[0]=a
    else:
        range_ab[1]=b
    print("\nupdated range:\t",range_ab)