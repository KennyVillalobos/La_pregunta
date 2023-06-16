import random

def generator(num_clauses, num_var, cases_number):
    vars = [i for i in range(1, num_var + 1)]
    used_vars = [False for i in vars]
    test_cases = []

    for i in range(cases_number):
        cnf = [[] for i in range(num_clauses)]
        clauses_not_full = [i for i in range(num_clauses)]

        for var in vars:
            clause = random.choice(clauses_not_full)
            cnf[clause].append(var)
            if len(cnf[clause]) == 3:
                clauses_not_full.remove(clause)

        for clause in clauses_not_full:
            missing_terms = 3 - len(cnf[clause])
            vars_unused = [var for var in vars]
            
            for var in cnf[clause]:
                vars_unused.remove(var)

            for
            
            
