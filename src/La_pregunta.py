def backtrack(boolean_exp: list[list[int]]):
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
