import calculations

def print_title(string: str):
	print("\u001b[107m--- ", string, " ---\u001b[0m")

def print_metrcs(designation: str, metric: str, value):
	print(" \u001b[94m", designation, "\u001b[0m	|", metric, ": ", value)

def print_hypothesis_testing(condition: bool):
	if (condition):
		print("\u001b[102mНет оснований для опровержения H₀\u001b[0m")
	else:
		print("\u001b[101mЕсть основания для опровержения H₀\u001b[0m")

# print sample info
def print_sample_stats(sample, index):
	D = calculations.find_general_variance(sample, calculations.find_average(sample))
	# print("\u001b[101m--- Sample ", index, "---\u001b[0m")
	print_title("Sample")
    
	print_metrcs("a_" + str(index), "Размер выборки", len(sample))
	print_metrcs("x̅_" + str(index), "Среднее значение", round(calculations.find_average(sample), 3))
	print_metrcs("s²_" + str(index), "Дисперсия выборки", round(D, 3))
	print_metrcs("s_" + str(index), "Cр. кв. отклонение выборки", round(D ** 0.5, 3))

# print info for list of samples
def print_sample_list_stats(samples_list):
	for i in range(0, len(samples_list)):
		print_sample_stats(samples_list[i], i + 1)