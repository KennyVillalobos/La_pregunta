from sympy import symbols

x,y = symbols('x,y')

print((x & ~y).subs({x:True, y:True}))

print("Format of the input\n")
print("& = and, | = or, ~ = not, >> = Implies\n")
formula = input("Type your formula\n")

formula = formula.split(" ")

