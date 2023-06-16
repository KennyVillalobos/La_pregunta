import random

def backtrack(boolean_exp):
    num_clauses = len(boolean_exp)
    vars_per_clause = len(boolean_exp[0])

    vars_values = {}

    for clause in boolean_exp:
            for term in clause:
                var = abs(term)
                vars_values[var] = False

    vars = list(vars_values.keys())
    vars_number = len(vars)

    def assing_values(expr, vars, vars_values, index, vars_number):
        if index == vars_number:
            clauses_values = []

            for clause in expr:
                clause_result = False
                for var in clause:
                    #the variables numbers start in 1
                    if var > 0:
                        clause_result = clause_result or vars_values[var]
                    else:
                        clause_result = clause_result or not vars_values[abs(var)]
                
                clauses_values.append(clause_result)

            result = all(clauses_values)
            if result:
                return vars_values, True
            else:
                return {}, False

        var = vars[index]
        vars_values[var] = True
        values, result = assing_values(expr, vars, vars_values, index + 1, vars_number)

        if result:
            return values, True
        
        else:
            vars_values[var] = False

        return assing_values(expr, vars, vars_values, index + 1, vars_number)

    result = assing_values(boolean_exp, vars, vars_values, 0, vars_number)

    return result    


#(greedy_criterion = 0) => Min of sat_clauses_for_var
#(greedy_criterion = 1) => Max of unsat_clauses_with_var
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
    for i in range(len(variables)):
        unsat_clauses_with_var[i] = 0
        sat_clauses_for_var[i] = 0
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
    print(p)
    if p < use_greedy_parameter:
        var_index = abs(random.choice(clauses[clause]))
        
    else:
        print('voy a usar un criterio greedy')
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
                sat = not variables[abs(var)-1]
            else:
                sat = variables[abs(var)-1]
            if sat:
                break
        if not sat_clauses[i] and sat:
            unsat_clauses.remove(i)
        sat_clauses[i] = sat
        
#print(walkSat([[1,2,3],[-1,-2,-3],[-1,2,3]],[False,False,False],50,1,0))
    