print("RegNo 2367413  Name:Nishant    Prog:Fibonacci method algorithim")
def function(x):
    result= x**4-14*(x**3)+60*(x**2)-70*x
    return result
range_ab=[0,2]
epslon=float(input("enter initial epselon value"))
E_value= ((1+2*epslon)/.15)
print("E=",E_value)
def fibonacci_series(E_value):
      n=[1,2]
      i=1
      while E_value>n[i]:
          new=(n[i-1]+n[i])
          n.append(new)
          i+=1
      return n
fb_series=fibonacci_series(E_value)
abc=len(fb_series)
n=abc-1
def ab(a0,b0,rho):
    a_next=a0+rho*(b0-a0)
    b_next=a0+(1-rho)*(b0-a0)
    return a_next,b_next
def rho(a,i):
    rh=1-(fb_series[a-i-2]/fb_series[a-i-1])
    return rh
for i in range(n):
    print(f"\nIteration No {i+1}")
    rh=rho(abc,i)
    if rh==0.5:
        rh-=.05
    a,b=ab(range_ab[0],range_ab[1],rh)
    f1=function(a)
    f2=function(b)
    print(f'f(a{i+1})= {f1},f(b{i+1})= {f2}')
    new=max(f1,f2)
    print("max=",new)
    if new==f1:
        range_ab[0]=a
    else:
        range_ab[1]=b
    print("updated range:\t",range_ab)