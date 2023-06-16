import sympy
from sympy.logic.boolalg import to_cnf

print("Format of the input\n")
print("& = and, | = or, ~ = not, >> = Implies, () = grouping\n")
formula = input("Type your formula\n")

formula = sympy.parse_expr(formula)
formula = str(to_cnf(formula))

clauses = formula.split('&')



print(formula)

