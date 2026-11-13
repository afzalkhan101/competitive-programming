# 244B · Undoubtedly Lucky Numbers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">bitmasks</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/244/B) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Polycarpus loves lucky numbers. Everybody knows that lucky numbers are positive integers, whose decimal representation (without leading zeroes) contain only the lucky digits x and y. For example, if x = 4, and y = 7, then numbers 47, 744, 4 are lucky.

Let's call a positive integer a undoubtedly lucky, if there are such digits x and y (0 ≤ x, y ≤ 9), that the decimal representation of number a (without leading zeroes) contains only digits x and y.

Polycarpus has integer n. He wants to know how many positive integers that do not exceed n, are undoubtedly lucky. Help him, count this number.

## Input

The first line contains a single integer n (1 ≤ n ≤ 109) — Polycarpus's number.

## Output

Print a single integer that says, how many positive integers that do not exceed n are undoubtedly lucky.

## Sample 1

Input

```text
10
```

Output

```text
10
```

## Sample 2

Input

```text
123
```

Output

```text
113
```

## Note

In the first test sample all numbers that do not exceed 10 are undoubtedly lucky.

In the second sample numbers 102, 103, 104, 105, 106, 107, 108, 109, 120, 123 are not undoubtedly lucky.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
