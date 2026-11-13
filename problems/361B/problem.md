# 361B · Levko and Permutation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/361/B) · Rating 1200

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Levko loves permutations very much. A permutation of length n is a sequence of distinct positive integers, each is at most n.

Let’s assume that value gcd(a, b) shows the greatest common divisor of numbers a and b. Levko assumes that element pi of permutation p1, p2, ... , pn is good if gcd(i, pi) > 1. Levko considers a permutation beautiful, if it has exactly k good elements. Unfortunately, he doesn’t know any beautiful permutation. Your task is to help him to find at least one of them.

## Input

The single line contains two integers n and k (1 ≤ n ≤ 105, 0 ≤ k ≤ n).

## Output

In a single line print either any beautiful permutation or -1, if such permutation doesn’t exist.

If there are multiple suitable permutations, you are allowed to print any of them.

## Sample 1

Input

```text
4 2
```

Output

```text
2 4 3 1
```

## Sample 2

Input

```text
1 1
```

Output

```text
-1
```

## Note

In the first sample elements 4 and 3 are good because gcd(2, 4) = 2 > 1 and gcd(3, 3) = 3 > 1. Elements 2 and 1 are not good because gcd(1, 2) = 1 and gcd(4, 1) = 1. As there are exactly 2 good elements, the permutation is beautiful.

The second sample has no beautiful permutations.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
