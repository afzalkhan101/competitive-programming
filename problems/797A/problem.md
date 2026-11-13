# 797A · k-Factorization

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/797/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Given a positive integer n, find k integers (not necessary distinct) such that all these integers are strictly greater than 1, and their product is equal to n.

## Input

The first line contains two integers n and k (2 ≤ n ≤ 100000, 1 ≤ k ≤ 20).

## Output

If it's impossible to find the representation of n as a product of k numbers, print -1.

Otherwise, print k integers in any order. Their product must be equal to n. If there are multiple answers, print any of them.

## Sample 1

Input

```text
100000 2
```

Output

```text
2 50000
```

## Sample 2

Input

```text
100000 20
```

Output

```text
-1
```

## Sample 3

Input

```text
1024 5
```

Output

```text
2 64 2 2 2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
