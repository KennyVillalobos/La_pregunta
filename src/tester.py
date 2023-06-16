from colorama import Fore
from La_pregunta import backtrack, walkSat
from test_cases_generator import generator

algorithm = {"1" : backtrack, "2" : walkSat}
generator = {"1" : generator}


print("Solutions:")
print("1: Backtrack", "2: WalkSat")
algo1 = input("Choose the first algorithm \n")
algo2 = input("Choose the second algorithm \n")

if algo1 == '2' or algo2 == '2':
    num_steps = int(input("Introduce the number of steps for WalkSat\n"))
    use_greedy_parameter = float(input("Introduce the greedy parameter for WalkSat\n"))
    greedy_criterion = int(input("Choose greedy criterion\n"))

gen = input("Choose the generator algorithm \n")

test_cases_number = int(input("How many test cases you want to generate? \n"))
number_variables = int(input("Set number of variables\n"))
number_of_clauses = int(input("Set number of clauses\n"))

test_cases = generator[gen](number_of_clauses, number_variables, test_cases_number)

if algo1 == algo2:
    if algo1 == '2':
        for case in test_cases:
            print(algorithm[algo1](case[0], case[1], num_steps, use_greedy_parameter, greedy_criterion))
    
    else:
        for case in test_cases:
            print(algorithm[algo1](case[0]))

else:
    wrong_cases = 0

    for case in test_cases:
        try:
            answer1 = algorithm[algo1](case[0])
            satisfacible1 = answer1[1]
        except:
            answer1 = algorithm[algo1](case[0], case[1], num_steps, use_greedy_parameter, greedy_criterion)
            satisfacible1 = not answer1[1]
        try:
            answer2 = algorithm[algo2](case[0])
            satisfacible2 = answer2[1]
        except:
            answer2 = algorithm[algo2](case[0], case[1], num_steps, use_greedy_parameter, greedy_criterion)
            satisfacible2 = not answer2[1]

        match = satisfacible1 == satisfacible2

        print(case)

        if match:
            print(Fore.GREEN, f"answer1:{answer1}, answer2:{answer2}, good")
            print(Fore.RESET, "\n")

        else:
            wrong_cases += 1
            print(Fore.RED, f"answer1:{answer1}, answer2:{answer2}, bad")
            print(Fore.RESET, "\n")

    print(f"Number of wrong cases: {wrong_cases} \n")