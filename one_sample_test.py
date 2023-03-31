import scipy.stats
import calculations
import print_tools
import sys
import operator

def perform_t_test(sample, alpha, hypothesis, operator0, operator1):
    print_tools.print_title("T-test")
    print(" H₀: μ₀ " + operator0 + " " + hypothesis)
    print(" H₁: μ₀ " + operator1 + " " + hypothesis)
    if (operator1 == '>' or operator1 == '<'):
        q = 1 - alpha / 2
    else:
        q = 1 - alpha
    t_crit = scipy.stats.t.ppf(q=q, df=len(sample) - 1)
    print_tools.print_metrcs("t_крит", "t критическое", round(t_crit, 3))
    if (not hypothesis.isnumeric()):
        exit()
    D = calculations.find_subgeneral_variance(sample, calculations.find_average(sample))
    t_obs = (calculations.find_average(sample) - float(hypothesis)) / ((D ** 0.5) / (len(sample) ** 0.5))
    print_tools.print_metrcs("t_набл", "t наблюдаемое", round(t_obs, 3))
    p_value = scipy.stats.t.sf(abs(t_obs), df=len(sample) - 1)
    if (operator1 == '!=' or operator1 == '='):
        p_value *= 2
    print_tools.print_metrcs("p-value", "p-value", round(p_value, 3))
    print_tools.print_hypothesis_testing(abs(t_obs) < t_crit)


def perform_z_test(sample, alpha, general_average, hypothesis, operator0, operator1):
    print_tools.print_title("Z-test")
    print(" H₀: μ₀ " + operator0 + " " + hypothesis)
    print(" H₁: μ₀ " + operator1 + " " + hypothesis)
    if (operator1 == '>' or operator1 == '<'):
        q = 1 - alpha / 2
    else:
        q = 1 - alpha
    z_crit = scipy.stats.norm.ppf(q)
    print_tools.print_metrcs("z_крит", "z критическое", round(z_crit, 3))
    z_obs = (calculations.find_average(sample) - float(hypothesis)) / (general_average / (len(sample) ** 0.5))
    print_tools.print_metrcs("z_набл", "z наблюдаемое" , round(z_obs, 3))
    p_value = scipy.stats.t.sf(abs(z_obs), df=len(sample) - 1)
    if (operator1 == '!=' or operator1 == '='):
        p_value *= 2
    print_tools.print_metrcs("p-value", "p-value", round(p_value, 3))
    print_tools.print_hypothesis_testing(abs(z_obs) < z_crit)

def one_sample_test(sample, alpha, general_average = None):
    hypothesis = input("Enter H₀ hypothesis value ")
    operator0 = input("Enter H₀ \u001b[91m\u001b[1mmain\u001b[0m hypothesis operator [>, <, !=, =] ")
    operator1 = input("Enter H₁ \u001b[91m\u001b[1malternative\u001b[0m hypothesis operator [>, <, !=, =] ")
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\033[F\033[K")
    if (operator0 not in ['>', '<', '!=', "="]):
        operator0 = '='
    if (operator1 not in ['>', '<', '!=', "="]):
        operator1 = '!='
    if (len(sample) < 30 or general_average == None):
        perform_t_test(sample, alpha, hypothesis, operator0, operator1)
    else:
        perform_z_test(sample, alpha, general_average, hypothesis, operator0, operator1)