<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 174A · Problem About Equation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/174/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

A group of n merry programmers celebrate Robert Floyd's birthday. Polucarpus has got an honourable task of pouring Ber-Cola to everybody. Pouring the same amount of Ber-Cola to everybody is really important. In other words, the drink's volume in each of the n mugs must be the same.

Polycarpus has already began the process and he partially emptied the Ber-Cola bottle. Now the first mug has a1 milliliters of the drink, the second one has a2 milliliters and so on. The bottle has b milliliters left and Polycarpus plans to pour them into the mugs so that the main equation was fulfilled.

Write a program that would determine what volume of the drink Polycarpus needs to add into each mug to ensure that the following two conditions were fulfilled simultaneously:

- there were b milliliters poured in total. That is, the bottle need to be emptied;
- after the process is over, the volumes of the drink in the mugs should be equal.

## Input

The first line contains a pair of integers n, b (2 ≤ n ≤ 100, 1 ≤ b ≤ 100), where n is the total number of friends in the group and b is the current volume of drink in the bottle. The second line contains a sequence of integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the current volume of drink in the i-th mug.

## Output

Print a single number "-1" (without the quotes), if there is no solution. Otherwise, print n float numbers c1, c2, ..., cn, where ci is the volume of the drink to add in the i-th mug. Print the numbers with no less than 6 digits after the decimal point, print each ci on a single line. Polycarpus proved that if a solution exists then it is unique.

Russian locale is installed by default on the testing computer. Make sure that your solution use the point to separate the integer part of a real number from the decimal, not a comma.

## Sample 1

Input

```text
5 50
1 2 3 4 5
```

Output

```text
12.000000
11.000000
10.000000
9.000000
8.000000
```

## Sample 2

Input

```text
2 2
1 100
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
