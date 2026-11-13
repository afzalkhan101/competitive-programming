# 456B · Fedya and Maths

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/456/B) · Rating 1200

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Fedya studies in a gymnasium. Fedya's maths hometask is to calculate the following expression:

(1n + 2n + 3n + 4n) mod 5

for given value of n. Fedya managed to complete the task. Can you? Note that given number n can be extremely large (e.g. it can exceed any integer type of your programming language).

## Input

The single line contains a single integer n (0 ≤ n ≤ 10105). The number doesn't contain any leading zeroes.

## Output

Print the value of the expression without leading zeros.

## Sample 1

Input

```text
4
```

Output

```text
4
```

## Sample 2

Input

```text
124356983594583453458888889
```

Output

```text
0
```

## Note

Operation x mod y means taking remainder after division x by y.

Note to the first sample:

$$( 1 ^ { 4 } + 2 ^ { 4 } + 3 ^ { 4 } + 4 ^ { 4 } ) \bmod 5 = ( 1 + 1 6 + 8 1 + 2 5 6 ) \bmod 5 = 4$$

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
