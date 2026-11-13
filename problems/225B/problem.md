# 225B · Well-known Numbers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">binary search</span><span class="practice-tag">greedy</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/225/B) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Numbers k-bonacci (k is integer, k > 1) are a generalization of Fibonacci numbers and are determined as follows:

- F(k, n) = 0, for integer n, 1 ≤ n < k;
- F(k, k) = 1;
- F(k, n) = F(k, n - 1) + F(k, n - 2) + ... + F(k, n - k), for integer n, n > k.

Note that we determine the k-bonacci numbers, F(k, n), only for integer values of n and k.

You've got a number s, represent it as a sum of several (at least two) distinct k-bonacci numbers.

## Input

The first line contains two integers s and k (1 ≤ s, k ≤ 109; k > 1).

## Output

In the first line print an integer m (m ≥ 2) that shows how many numbers are in the found representation. In the second line print m distinct integers a1, a2, ..., am. Each printed integer should be a k-bonacci number. The sum of printed integers must equal s.

It is guaranteed that the answer exists. If there are several possible answers, print any of them.

## Sample 1

Input

```text
5 2
```

Output

```text
3
0 2 3
```

## Sample 2

Input

```text
21 5
```

Output

```text
3
4 1 16
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
