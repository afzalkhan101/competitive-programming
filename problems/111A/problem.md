# 111A · Petya and Inequiations

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/111/A) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Little Petya loves inequations. Help him find n positive integers a1, a2, ..., an, such that the following two conditions are satisfied:

- a12 + a22 + ... + an2 ≥ x
- a1 + a2 + ... + an ≤ y

## Input

The first line contains three space-separated integers n, x and y (1 ≤ n ≤ 105, 1 ≤ x ≤ 1012, 1 ≤ y ≤ 106).

Please do not use the %lld specificator to read or write 64-bit integers in С++. It is recommended to use cin, cout streams or the %I64d specificator.

## Output

Print n positive integers that satisfy the conditions, one integer per line. If such numbers do not exist, print a single number "-1". If there are several solutions, print any of them.

## Sample 1

Input

```text
5 15 15
```

Output

```text
4
4
1
1
2
```

## Sample 2

Input

```text
2 3 2
```

Output

```text
-1
```

## Sample 3

Input

```text
1 99 11
```

Output

```text
11
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
