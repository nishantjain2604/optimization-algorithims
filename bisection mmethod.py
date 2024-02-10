from sympy import symbols, diff, simplify
#equation_str = input("Enter an equation in terms of 'x': ")
x = symbols('x')
equation_str=x**4-14*(x**3)+60*(x**2)-70*x
derivative = diff(equation_str, x)
range_ab=[0,2]
wish_range=.3
n=0
while (.5)**n>(wish_range/2):
    midP=(range_ab[0]+range_ab[1])/2
    fxi=derivative.subs(x,midP)
    print(f'f{n+1}=',fxi)
    if fxi>0:
        range_ab[1]=midP
    else:
        range_ab[0]=midP
    print(f'updated range is {range_ab}')
    n+=1