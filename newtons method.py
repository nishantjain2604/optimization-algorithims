from sympy import symbols, diff, simplify
#equation_str = input("Enter an equation in terms of 'x': ")
#equation_str=x**4-14*(x**3)+60*(x**2)-70*x
x = symbols('x')
equation_str=x**3-12.2*(x**2)+7.45*(x)+42
derivative = diff(equation_str, x)
print("d",derivative)
derivative_2nd=diff(derivative, x)
print("d2",derivative_2nd)
xi=12
accuracy=5
def xnext(x0):
    x1=x0-(derivative.subs(x, x0)/derivative_2nd.subs(x ,x0))
    return x1
x0=round(xnext(xi),accuracy)
print(f'x{0}= {x0}')
i=0
while True:
    i += 1
    xn=round(xnext(x0),accuracy)
    print(f'\nx{i}= {xn}')
    if x0==xn:
        break
    else:
        x0=xn
