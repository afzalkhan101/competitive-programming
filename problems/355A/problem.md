# 355A · Vasya and Digital Root

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/355/A) · Rating 1100

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Vasya has recently found out what a digital root of a number is and he decided to share his knowledge with you.

Let's assume that S(n) is the sum of digits of number n, for example, S(4098) = 4 + 0 + 9 + 8 = 21. Then the digital root of number n equals to:

1. dr(n) = S(n), if S(n) < 10;
2. dr(n) = dr( S(n) ), if S(n) ≥ 10.

For example, dr(4098)  =  dr(21)  =  3.

Vasya is afraid of large numbers, so the numbers he works with are at most 101000. For all such numbers, he has proved that dr(n)  =  S( S( S( S(n) ) ) ) (n ≤ 101000).

Now Vasya wants to quickly find numbers with the given digital root. The problem is, he hasn't learned how to do that and he asked you to help him. You task is, given numbers k and d, find the number consisting of exactly k digits (the leading zeroes are not allowed), with digital root equal to d, or else state that such number does not exist.

## Input

The first line contains two integers k and d (1 ≤ k ≤ 1000; 0 ≤ d ≤ 9).

## Output

In a single line print either any number that meets the requirements (without the leading zeroes) or "No solution" (without the quotes), if the corresponding number does not exist.

The chosen number must consist of exactly k digits. We assume that number 0 doesn't contain any leading zeroes.

## Sample 1

Input

```text
4 4
```

Output

```text
5881
```

## Sample 2

Input

```text
5 1
```

Output

```text
36172
```

## Sample 3

Input

```text
1 0
```

Output

```text
0
```

## Note

For the first test sample dr(5881)  =  dr(22)  =  4.

For the second test sample dr(36172)  =  dr(19)  =  dr(10)  =  1.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
