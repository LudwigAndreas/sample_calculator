import scipy.stats
import calculations
import print_tools

def perform_one_way_anova(samples, alpha):
    print_tools.print_title("One-way ANOVA test")
    print(" H₀: μ₀ = μ₁ = μ₂ = ... = μₙ")
    print(" H₁: There will be at least one population mean that differs from the rest")
    means = []
    size = 0
    for sample in samples:
        means.append(calculations.find_average(sample))
        size += len(sample)
    general_mean = calculations.find_average(means)
    print_tools.print_metrcs("x̅", "Общее среднее значение", round(general_mean, 3))

    print_tools.print_metrcs("a", "Общий размер", round(size, 3))
    ssb = 0
    ssw = 0
    for i in range(0, len(samples)):
        ssb += len(samples[i]) * ((means[i] - general_mean) ** 2)
        for j in range(0, len(samples[i])):
            ssw += (samples[i][j] - means[i]) ** 2
    print_tools.print_metrcs("SSB", "Межгрупповая сумма квадратов", round(ssb, 3))
    print_tools.print_metrcs("SSW", "Сумма квадратов внутри групп", round(ssw, 3))
    dfb = len(samples) - 1
    print_tools.print_metrcs("dfb", "Степени свобды между групп", round(dfb, 3))
    dfw = size - len(samples)
    print_tools.print_metrcs("dfw", "Степени свобды внутри групп", round(dfw, 3))
    msb = ssb / dfb
    print_tools.print_metrcs("msb", "Средний квадрат отклонения между групп", round(msb, 3))
    msw = ssw / dfw
    print_tools.print_metrcs("msw", "Средний квадрат отклонения внутри групп", round(msw, 3))
    f_crit = scipy.stats.f.ppf(1 - alpha, dfb, dfw)
    print_tools.print_metrcs("F_крит", "Критическое значение критерия фишера", round(f_crit, 3))
    f_obs = msb / msw
    print_tools.print_metrcs("F_наб", "Значение критерия фишера", round(f_obs, 3))
    print_tools.print_hypothesis_testing(abs(f_obs) < f_crit)

def multiple_sample_tests(samples, alpha):
    perform_one_way_anova(samples, alpha)