import argparse
import calculations
import one_sample_test
import two_sample_test
import multi_sample_test
import print_tools

# reading sample from file
def read_int_list_from_file(file_path):
	with open(file_path, 'r') as f:
		line = f.readline().strip()
		int_list = [float(x) for x in line.split()]
		return int_list


if __name__ == '__main__':
	# create the ArgumentParser object
	parser = argparse.ArgumentParser(prog='calculator', description='Little calculator for standard statistics operations with samples')
	requiredNamed=parser.add_argument_group('Required named arguments')

	# add the arguments
	requiredNamed.add_argument('-s', '--samples', nargs='+', type=str, help='file or files that contains list of samples', required=True)
	parser.add_argument('-a', '--alpha', type=float, help='alpha [α]')
	parser.add_argument('-g', '--general_average', nargs='*', type=float, help='set general average or list of general averages if there is multiply samples [σ²]')

	# parse the arguments
	args = parser.parse_args()

	# read samples and output info
	samples = [read_int_list_from_file(file_path) for file_path in args.samples]
	general_averages = args.general_average
	print_tools.print_sample_list_stats(samples)

	alpha = args.alpha

	if (len(samples) == 1):
		print_tools.print_title("One Sample Test")
		if (general_averages != None):
			one_sample_test.one_sample_test(samples[0], alpha, general_averages[0])
		else:
			one_sample_test.one_sample_test(samples[0], alpha,)
	elif (len(samples) == 2):
		print_tools.print_title("Two Sample Test")
		if (alpha == None):
			two_sample_test.correlation_analysis(samples[0], samples[1])
		elif (general_averages != None and general_averages[0] != None and general_averages[1] != None):
			two_sample_test.two_sample_tests(samples[0], samples[1], alpha, general_average1=general_averages[0], general_average2=general_averages[1])
		else:
			two_sample_test.two_sample_tests(samples[0], samples[1], alpha)
		
	else:
		print_tools.print_title("Multiple Sample Test")
		multi_sample_test.multiple_sample_tests(samples, alpha)