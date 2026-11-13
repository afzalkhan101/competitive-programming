# 359C · Prime Number

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/359/C) · Rating 1900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Simon has a prime number x and an array of non-negative integers a1, a2, ..., an.

Simon loves fractions very much. Today he wrote out number $$\frac{1}{x^{a_1}} + \frac{1}{x^{a_2}} + \ldots + \frac{1}{x^{a_n}}$$ on a piece of paper. After Simon led all fractions to a common denominator and summed them up, he got a fraction: $$\text{S}$$, where number t equals xa1 + a2 + ... + an. Now Simon wants to reduce the resulting fraction.

Help him, find the greatest common divisor of numbers s and t. As GCD can be rather large, print it as a remainder after dividing it by number 1000000007 (109 + 7).

## Input

The first line contains two positive integers n and x (1 ≤ n ≤ 105, 2 ≤ x ≤ 109) — the size of the array and the prime number.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ a1 ≤ a2 ≤ ... ≤ an ≤ 109).

## Output

Print a single number — the answer to the problem modulo 1000000007 (109 + 7).

## Sample 1

Input

```text
2 2
2 2
```

Output

```text
8
```

## Sample 2

Input

```text
3 3
1 2 3
```

Output

```text
27
```

## Sample 3

Input

```text
2 2
29 29
```

Output

```text
73741817
```

## Sample 4

Input

```text
4 5
0 0 0 0
```

Output

```text
1
```

## Note

In the first sample $$\frac{1}{4} + \frac{1}{4} = \frac{4+4}{16} = \frac{8}{16}$$. Thus, the answer to the problem is 8.

In the second sample, $$\frac{1}{3}+\frac{1}{9}+\frac{1}{27}=\frac{243+81+27}{729}=\frac{351}{729}$$. The answer to the problem is 27, as 351 = 13·27, 729 = 27·27.

In the third sample the answer to the problem is 1073741824 mod 1000000007 = 73741817.

In the fourth sample $$\frac{1}{1}+\frac{1}{1}+\frac{1}{1}+\frac{1}{1}=\frac{4}{1}$$. Thus, the answer to the problem is 1.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
