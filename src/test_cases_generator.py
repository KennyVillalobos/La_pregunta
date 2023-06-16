import random

def generator(num_clauses, num_var, cases_number):
    vars = [i for i in range(1, num_var + 1)]
    used_vars = [False for i in vars]
    test_cases = []
    clauses_not_full = [i for i in range(num_clauses)]

    for i in range(cases_number):
        cnf = [[] for i in range(num_clauses)]
        for j in vars:
            clause = random.choice(clauses_not_full)
            
            
