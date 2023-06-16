import sympy
from sympy.logic.boolalg import to_cnf


def cnf_to_list(formula):
    formula = "~(" + formula + ")"
    formula = sympy.parse_expr(formula)
    formula = str(to_cnf(formula))

    vars_count = 1
    clause_index = 0
    vars = {}
    is_negative = False
    cnf = [[]]

    for token in formula:
        if token not in ['(', ')', ' ', '&', '|']:
            if token == '~':
                is_negative = True
                continue

            if token not in vars.keys():
                vars[token] = vars_count
                vars_count += 1

            if is_negative:
                cnf[clause_index].append(-vars[token])
                is_negative = False
            else:
                cnf[clause_index].append(vars[token])

        if token == '&':
            cnf.append([])
            clause_index += 1

    new_vars = list(vars.values())

    return cnf, new_vars