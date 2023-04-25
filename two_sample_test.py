import calculations
import scipy.stats
import print_tools

def perform_f_test(sample1, sample2, alpha) -> bool:
    D0 = calculations.find_subgeneral_variance(sample1, calculations.find_average(sample1))
    D1 = calculations.find_subgeneral_variance(sample2, calculations.find_average(sample2))
    print_tools.print_title("F-test")
    print(" H₀: σ₀ = σ₁")
    print(" H₁: σ₀ ≠ σ₁")
    k_1 = max(len(sample1), len(sample2)) - 1
    k_2 = min(len(sample1), len(sample2)) - 1
    print_tools.print_metrcs("k₁", "k₁", k_1)
    print_tools.print_metrcs("k₂", "k₂", k_2)
    f_crit = scipy.stats.f.ppf(1 - alpha / 2, k_1, k_2)
    print_tools.print_metrcs("F_крит", "F критическое", round(f_crit, 3))
    f_obs = max(D0, D1) / min(D0, D1)
    print_tools.print_metrcs("F_набл", "F наблюдаемое", round(f_obs, 3))
    print_tools.print_hypothesis_testing(abs(f_obs) < f_crit)
    return abs(f_obs) < f_crit

def perform_t_test(sample1, sample2 , alpha) -> bool:
    print_tools.print_title("T-test")
    print(" H₀: μ₀ = μ₁")
    print(" H₁: μ₀ ≠ μ₁")
    x1 = calculations.find_average(sample1)
    x2 = calculations.find_average(sample2)
    D0 = calculations.find_subgeneral_variance(sample1, x1)
    D1 = calculations.find_subgeneral_variance(sample2, x2)
    t_crit = scipy.stats.t.ppf(q= 1 - alpha / 2, df=len(sample1) + len(sample2) - 2)
    s_general = ((D0 * (len(sample1) - 1) + D1 * (len(sample2) - 1)) / (len(sample1) + len(sample2) - 2)) ** 0.5
    print_tools.print_metrcs("S_общ", "S общее", round(s_general, 3))
    print_tools.print_metrcs("t_крит", "t критическое", round(t_crit, 3))
    t_obs = (x1 - x2) / (s_general * ((1 / len(sample1) + 1 / len(sample2)) ** 0.5))
    print_tools.print_metrcs("t_набл", "t наблюдаемое", round(t_obs, 3))
    print_tools.print_hypothesis_testing(abs(t_obs) < t_crit)

def perform_z_test(sample1, sample2, alpha, general_average1 = None, general_average2 = None) -> bool:
    print_tools.print_title("Z-test")
    print(" H₀: μ₀ = μ₁")
    print(" H₁: μ₀ ≠ μ₁") # TODO mean1 and mean2 may be different
    x1 = calculations.find_average(sample1)
    x2 = calculations.find_average(sample2)
    D0 = calculations.find_subgeneral_variance(sample1, x1)
    D1 = calculations.find_subgeneral_variance(sample2, x2)
    z_crit = scipy.stats.norm.ppf(1 - alpha / 2)
    print_tools.print_metrcs("z_крит", "z критическое", round(z_crit, 3))
    if (general_average1 != None and general_average2 != None):
        D0 = general_average1
        D1 = general_average2
    # z_obs = ((x1 - x2) - (mean1 - mean2)) / ((D0 / len(sample1) + D1 / len(sample2)) ** 0.5)
    z_obs = (x1 - x2) / ((D0 / len(sample1) + D1 / len(sample2)) ** 0.5)
    print_tools.print_metrcs("t_набл", "t наблюдаемое", round(z_obs, 3))
    print_tools.print_hypothesis_testing(abs(z_obs) < z_crit)


def two_sample_tests(sample1, sample2, alpha, general_average1 = None, general_average2 = None):
    if (len(sample1) < 30 and len(sample2) < 30):
        if (perform_f_test(sample1, sample2, alpha)):
            perform_t_test(sample1, sample2, alpha)
            exit()
    perform_z_test(sample1, sample2, alpha, general_average1, general_average2)


def correlation_analysis(x, y):
	print_tools.print_title("Correlation analysis")
	sum_x = sum(x)
	sum_y = sum(y)
	sum_x_min_y = 0
	sum_xy = 0
	sum_x_sqr = 0
	sum_y_sqr = 0
	n = len(x)
	S = 0;
	xy = []
	sqr_x = []
	for i in range(n):
		sum_xy += x[i] * y[i]
		sqr_x.append(x[i] ** 2)
		xy.append(x[i] * y[i])
		sum_x_sqr += x[i] ** 2
		sum_y_sqr += y[i] ** 2
		sum_x_min_y += x[i] - y[i]
	av_x = calculations.find_average(x)
	av_y = calculations.find_average(y)
	av_xy = calculations.find_average(xy)
	av_sqr_x = calculations.find_average(sqr_x)

	b1 = (av_xy - av_x * av_y) / (av_sqr_x - (av_x ** 2))
	b0 = av_y - b1 * av_x

	Dy = calculations.find_general_variance(y, av_y)
	Dx = calculations.find_general_variance(x, av_x)

	r = (av_xy - av_x * av_y) / ((Dx ** 0.5) * (Dy ** 0.5))

	print_tools.print_metrcs("xy", "", round(calculations.find_average(xy), 3))
	print_tools.print_metrcs("sum(x)", "", sum_x)
	print_tools.print_metrcs("sum(y)", "", sum_y)
	print_tools.print_metrcs("sum(xy)", "", round(sum_xy, 3))
	print_tools.print_metrcs("sum(x²)", "", round(sum_x_sqr, 3))
	print_tools.print_metrcs("sum(y²)", "", round(sum_y_sqr, 3))
	print_tools.print_metrcs("b0", "", round(b0, 3))
	print_tools.print_metrcs("b1", "", round(b1, 3))
	print_tools.print_metrcs("r", "", round(r, 3))