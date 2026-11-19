<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 858A · k-rounding

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/858/A) · Rating 1100

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

For a given positive integer n denote its k-rounding as the minimum positive integer x, such that x ends with k or more zeros in base 10 and is divisible by n.

For example, 4-rounding of 375 is 375·80 = 30000. 30000 is the minimum integer such that it ends with 4 or more zeros and is divisible by 375.

Write a program that will perform the k-rounding of n.

## Input

The only line contains two integers n and k (1 ≤ n ≤ 109, 0 ≤ k ≤ 8).

## Output

Print the k-rounding of n.

## Sample 1

Input

```text
375 4
```

Output

```text
30000
```

## Sample 2

Input

```text
10000 1
```

Output

```text
10000
```

## Sample 3

Input

```text
38101 0
```

Output

```text
38101
```

## Sample 4

Input

```text
123456789 8
```

Output

```text
12345678900000000
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
