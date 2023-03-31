
# среднее значение
def find_average(x):
	return sum(x) / len(x)

# размах
def find_range(x):
	x_copy = sorted(x)
	return abs(x_copy[-1] - x_copy[0])

# медиана
def find_median(x):
	if (len(x) % 2 != 0):
		return (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
	else:
		return x[len(x) // 2]

# 0,5 квартиль
def find_05_quartile(x):
	return find_median(x)

# 0,25 квартиль
def find_025_quartile(x):
	return x[len(x) * 3 // 4]

# 0,75 квартиль
def find_075_quartile(x):
	return x[len(x) // 4]

# дисперсия генеральной совокупности
def find_general_variance(x, x_average):
	variance = 0
	for i in x:
		variance += (i - x_average) ** 2
	return variance / len(x)

# дисперсия выборки
def find_subgeneral_variance(x, x_average):
	variance = 0
	for i in x:
		variance += (i - x_average) ** 2
	return variance / (len(x) - 1)


