from La_pregunta import walkSat, backtrack
from utils import cnf_to_list

print("Format of the input\n")
print("& = and, | = or, ~ = not, >> = Implies, () = grouping\n")
formula = input("Type your formula\n")

cnf, vars = cnf_to_list(formula)

print("Bactrack result:\n")
print(str(backtrack(cnf)) + '\n')

print("WalkSat result:\n")
print(walkSat(cnf, vars, 100*len(vars), 0.5, 0))

