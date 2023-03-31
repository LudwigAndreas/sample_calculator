# Little sample calculator

Little sample calculator written on python using scipy. It may calculate standard metrics for samples, test one-sample, two-samples and multiple-samples hypotheses.

## Installation

    git clone https://github.com/LudwigAndreas/sample_calculator.git

Note that you will need to have the required dependencies installed, as listed in the `requirements.txt` file. You can install them using the following command:

    pip install -r requirements.txt


## Usage

```
$ python3 main.py [-h] -s SAMPLES [SAMPLES ...] [-a ALPHA] [-g [GENERAL_AVERAGE ...]]

options:
  -h, --help            show this help message and exit
  -a ALPHA, --alpha ALPHA
                        set alpha value for tests [α]
  -g [GENERAL_AVERAGE ...], --general_average [GENERAL_AVERAGE ...]
                        set general average or list of general averages if there is multiply samples [σ²]

Required named arguments:
  -s SAMPLES [SAMPLES ...], --samples SAMPLES [SAMPLES ...]
                        file or files that contains list of samples
```
Alternatively, you can start the program using the `start.sh` Bash script provided in the repository. The script will start the program with any command-line arguments you pass to it.

To use the script, make sure you have execute permission by running `chmod +x start.sh`. Then, you can start the program with the desired arguments by running the following command in the terminal:

```
./start.sh [-h] -s SAMPLES [SAMPLES ...] [-a ALPHA] [-g [GENERAL_AVERAGE ...]]
```


## Examples

```
$ python3 main.py -s values_1 -a 0.05
---  Sample  ---
  a_1   | Размер выборки :  11
  x̅_1   | Среднее значение :  13.636
  s²_1  | Дисперсия выборки :  5.504
  s_1   | Cр. кв. отклонение выборки :  2.346
---  One Sample Test  ---
---  T-test  ---
 H₀: μ₀ = 10
 H₁: μ₀ != 10
  t_крит        | t критическое :  1.812
  t_набл        | t наблюдаемое :  4.901
  p-value       | p-value :  0.001
Есть основания для опровержения H₀
```
```
$ python3 main.py -s values_1 values_2 -a 0.05
---  Sample  ---
  a_1   | Размер выборки :  11
  x̅_1   | Среднее значение :  13.636
  s²_1  | Дисперсия выборки :  5.504
  s_1   | Cр. кв. отклонение выборки :  2.346
---  Sample  ---
  a_2   | Размер выборки :  9
  x̅_2   | Среднее значение :  9.444
  s²_2  | Дисперсия выборки :  4.247
  s_2   | Cр. кв. отклонение выборки :  2.061
---  Two Sample Test  ---
---  F-test  ---
 H₀: σ₀ = σ₁
 H₁: σ₀ ≠ σ₁
  k₁    | k₁ :  10
  k₂    | k₂ :  8
  F_крит        | F критическое :  3.347
  F_набл        | F наблюдаемое :  1.267
Нет оснований для опровержения H₀
---  T-test  ---
 H₀: μ₀ = μ₁
 H₁: μ₀ ≠ μ₁
  t_крит        | t критическое :  2.101
  t_набл        | t наблюдаемое :  3.981
Есть основания для опровержения H₀
```
```
$ python3 main.py -s anova_1 anova_2 anova_3 -a 0.05 
---  Sample  ---
  a_1   | Размер выборки :  3
  x̅_1   | Среднее значение :  2.0
  s²_1  | Дисперсия выборки :  0.667
  s_1   | Cр. кв. отклонение выборки :  0.816
---  Sample  ---
  a_2   | Размер выборки :  3
  x̅_2   | Среднее значение :  4.0
  s²_2  | Дисперсия выборки :  0.667
  s_2   | Cр. кв. отклонение выборки :  0.816
---  Sample  ---
  a_3   | Размер выборки :  3
  x̅_3   | Среднее значение :  6.0
  s²_3  | Дисперсия выборки :  0.667
  s_3   | Cр. кв. отклонение выборки :  0.816
---  Multiple Sample Test  ---
---  One-way ANOVA test  ---
 H₀: μ₀ = μ₁ = μ₂ = ... = μₙ
 H₁: There will be at least one population mean that differs from the rest
  x̅     | Общее среднее значение :  4.0
  a     | Общий размер :  9
  SSB   | Межгрупповая сумма квадратов :  24.0
  SSW   | Сумма квадратов внутри групп :  6.0
  dfb   | Степени свобды между групп :  2
  dfw   | Степени свобды внутри групп :  6
  msb   | Средний квадрат отклонения между групп :  12.0
  msw   | Средний квадрат отклонения внутри групп :  1.0
  F_крит        | Критическое значение критерия фишера :  5.143
  F_наб         | Значение критерия фишера :  12.0
Есть основания для опровержения H₀
```

## Contributing

We welcome contributions from anyone who would like to help improve this project. If you'd like to contribute, please follow these guidelines:

* Fork the repository and create your branch from main.
* Write clear, concise code and comments.
* Test your changes thoroughly before submitting a pull request.
* Make sure your code follows the project's coding conventions.
* Ensure that your pull request includes a clear description of the problem or feature, and how it improves the project.
* Wait for one of the maintainers to review your code and provide feedback.
* Once your code has been reviewed and approved, it will be merged into the main branch.

Thank you for your interest in contributing to this project!

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

## Acknowledgments

We would like to thank the following individuals and organizations for their contributions to this project:

* Mukhamedjanova Sofia, for providing valuable feedback during the development process.

## Contact

If you have any questions, comments, or feedback about this project, you can reach us at:

* Email: ev.sand.raw@gmail.com
* Telegram: @Ludwig_Andreas
* GitHub: @LudwigAndreas

We would love to hear from you!