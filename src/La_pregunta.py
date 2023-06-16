import random

def walkSat(clauses, variables, number_of_steps, use_greedy_parameter, greedy_criterion):
    unsat_clauses_with_var = [0 for i in range(len(variables))]
    sat_clauses_for_var = [0 for i in range(len(variables))]
    sat_clauses = variable_assigment(clauses, variables)
    unsat_clauses = []
    if check_sat(clauses, variables, sat_clauses, unsat_clauses, unsat_clauses_with_var, sat_clauses_for_var):
        return (variables, len(unsat_clauses))
    for i in range(number_of_steps):
        print(f'{i+1} pasos de WalkSat, distribucion actual:{variables}')
        step(clauses, variables, unsat_clauses, sat_clauses, use_greedy_parameter, greedy_criterion, unsat_clauses_with_var, sat_clauses_for_var )
        if check_sat(clauses, variables, sat_clauses, unsat_clauses, unsat_clauses_with_var, sat_clauses_for_var):
            return (variables, len(unsat_clauses))
    return (variables, len(unsat_clauses))
    
    
    
def variable_assigment(clauses, variables):
    for i in range(len(variables)):
        variables[i] = True if random.randint(0,1) == 1 else False
    sat_clauses = [False for i in range(len(clauses))]
    
    for i in range(len(clauses)):
        sat = 1
        for var in clauses[i]:
            if var<0:
                sat = not variables[abs(var)-1]
            else:
                sat = variables[abs(var)-1]
            if sat:
                break
        sat_clauses[i] = sat
    return sat_clauses

def check_sat(clauses, variables, sat_clauses, unsat_clauses, unsat_clauses_with_var, sat_clauses_for_var):
    sat = 0
    unsat_clauses.clear()
    for i in range(len(sat_clauses)):
        if sat_clauses[i]:
            sat = sat + 1
            one_var_sat = 0
            var_sat_clause = 0
            for var in clauses[i]:
                if var<0:
                    if not variables[abs(var)-1]:
                        one_var_sat = one_var_sat + 1
                        var_sat_clause = abs(var)
                else:
                    if variables[abs(var)-1]:
                        one_var_sat = one_var_sat + 1
                        var_sat_clause = abs(var)
                if one_var_sat > 1:
                    break
            if one_var_sat == 1:
                sat_clauses_for_var[var_sat_clause-1] = sat_clauses_for_var[var_sat_clause-1] + 1
                    
        else:
            unsat_clauses.append(i)
            for var in clauses[i]:
                var_index = abs(var)
                unsat_clauses_with_var[var_index-1] = unsat_clauses_with_var[var_index-1] + 1
    return sat == len(sat_clauses)

def step(clauses, variables, unsat_clauses, sat_clauses, use_greedy_parameter, greedy_criterion, unsat_clauses_with_var, sat_clauses_for_var):
    clause = random.choice(unsat_clauses)
    p = random.randint(0,100) /100
    
    if p < use_greedy_parameter:
        var_index = abs(random.choice(clauses[clause]))
        
    else:
        if greedy_criterion == 0: # Min of sat_clauses_for_var
            var_index = 0
            number_of_clauses = len(clauses) + 1
            for var in clauses[clause]:
                if sat_clauses_for_var[abs(var)-1] < number_of_clauses:
                    number_of_clauses =  sat_clauses_for_var[abs(var)-1]
                    var_index = abs(var)
        else: # Max of unsat_clauses_with_var
            var_index = 0
            number_of_clauses = -1
            for var in clauses[clause]:
                if unsat_clauses_with_var[abs(var)-1] > number_of_clauses:
                    number_of_clauses = unsat_clauses_with_var[abs(var)-1]
                    var_index = abs(var)
    
    variables[var_index-1] = not variables[var_index-1]
    
    for i in range(len(clauses)):
        sat = False
        for var in clauses[i]:
            if var<0:
                sat = not variables[var-1]
            else:
                sat = variables[var-1]
            if sat:
                break
        if not sat_clauses[i] and sat:
            unsat_clauses.remove(i)
        sat_clauses[i] = sat
        
print(walkSat([[1,2,3],[-1,-2,-3],[-1,2,3]],[False,False,False],50,1,0))
    