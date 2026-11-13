# 236B · Easy Number Challenge

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">implementation</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/236/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Let's denote d(n) as the number of divisors of a positive integer n. You are given three integers a, b and c. Your task is to calculate the following sum:

$$\sum_{i=1}^{a}\sum_{j=1}^{b}\sum_{k=1}^{c}d(i \cdot j \cdot k)$$

Find the sum modulo 1073741824 (230).

## Input

The first line contains three space-separated integers a, b and c (1 ≤ a, b, c ≤ 100).

## Output

Print a single integer — the required sum modulo 1073741824 (230).

## Sample 1

Input

```text
2 2 2
```

Output

```text
20
```

## Sample 2

Input

```text
5 6 7
```

Output

```text
1520
```

## Note

For the first example.

- d(1·1·1) = d(1) = 1;
- d(1·1·2) = d(2) = 2;
- d(1·2·1) = d(2) = 2;
- d(1·2·2) = d(4) = 3;
- d(2·1·1) = d(2) = 2;
- d(2·1·2) = d(4) = 3;
- d(2·2·1) = d(4) = 3;
- d(2·2·2) = d(8) = 4.

So the result is 1 + 2 + 2 + 3 + 2 + 3 + 3 + 4 = 20.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
