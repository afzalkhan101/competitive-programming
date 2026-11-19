<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 58B · Coins

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/58/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

In Berland a money reform is being prepared. New coins are being introduced. After long economic calculations was decided that the most expensive coin should possess the denomination of exactly n Berland dollars. Also the following restriction has been introduced for comfort: the denomination of each coin should be divisible by the denomination of any cheaper coin. It is known that among all the possible variants the variant with the largest number of new coins will be chosen. Find this variant. Print in the order of decreasing of the coins' denominations.

## Input

The first and only line contains an integer n (1 ≤ n ≤ 106) which represents the denomination of the most expensive coin.

## Output

Print the denominations of all the coins in the order of decreasing. The number of coins must be the largest possible (with the given denomination n of the most expensive coin). Also, the denomination of every coin must be divisible by the denomination of any cheaper coin. Naturally, the denominations of all the coins should be different. If there are several solutins to that problem, print any of them.

## Sample 1

Input

```text
10
```

Output

```text
10 5 1
```

## Sample 2

Input

```text
4
```

Output

```text
4 2 1
```

## Sample 3

Input

```text
3
```

Output

```text
3 1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
