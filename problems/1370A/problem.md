<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 1370A · Maximum GCD

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1370/A) · Rating 800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Let's consider all integers in the range from $$$1$$$ to $$$n$$$ (inclusive).

Among all pairs of distinct integers in this range, find the maximum possible greatest common divisor of integers in pair. Formally, find the maximum value of $$$\mathrm{gcd}(a, b)$$$, where $$$1 \leq a < b \leq n$$$.

The greatest common divisor, $$$\mathrm{gcd}(a, b)$$$, of two positive integers $$$a$$$ and $$$b$$$ is the biggest integer that is a divisor of both $$$a$$$ and $$$b$$$.

## Input

The first line contains a single integer $$$t$$$ ($$$1 \leq t \leq 100$$$)  — the number of test cases. The description of the test cases follows.

The only line of each test case contains a single integer $$$n$$$ ($$$2 \leq n \leq 10^6$$$).

## Output

For each test case, output the maximum value of $$$\mathrm{gcd}(a, b)$$$ among all $$$1 \leq a < b \leq n$$$.

## Sample 1

Input

```text
2
3
5
```

Output

```text
1
2
```

## Note

In the first test case, $$$\mathrm{gcd}(1, 2) = \mathrm{gcd}(2, 3) = \mathrm{gcd}(1, 3) = 1$$$.

In the second test case, $$$2$$$ is the maximum possible value, corresponding to $$$\mathrm{gcd}(2, 4)$$$.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
