<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 385C · Bear and Prime Numbers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">binary search</span><span class="practice-tag">brute force</span><span class="practice-tag">data structures</span><span class="practice-tag">dp</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/385/C) · Rating 1700

Time: 2.0 seconds · Memory: 512.0 MB

## Problem

Recently, the bear started studying data structures and faced the following problem.

You are given a sequence of integers x1, x2, ..., xn of length n and m queries, each of them is characterized by two integers li, ri. Let's introduce f(p) to represent the number of such indexes k, that xk is divisible by p. The answer to the query li, ri is the sum: $$\sum_{p \in S(l_i, r_i)} f(p)$$, where S(li, ri) is a set of prime numbers from segment [li, ri] (both borders are included in the segment).

Help the bear cope with the problem.

## Input

The first line contains integer n (1 ≤ n ≤ 106). The second line contains n integers x1, x2, ..., xn (2 ≤ xi ≤ 107). The numbers are not necessarily distinct.

The third line contains integer m (1 ≤ m ≤ 50000). Each of the following m lines contains a pair of space-separated integers, li and ri (2 ≤ li ≤ ri ≤ 2·109) — the numbers that characterize the current query.

## Output

Print m integers — the answers to the queries on the order the queries appear in the input.

## Sample 1

Input

```text
6
5 5 7 10 14 15
3
2 11
3 12
4 4
```

Output

```text
9
7
0
```

## Sample 2

Input

```text
7
2 3 5 7 11 4 8
2
8 10
2 123
```

Output

```text
0
7
```

## Note

Consider the first sample. Overall, the first sample has 3 queries.

1. The first query l = 2, r = 11 comes. You need to count f(2) + f(3) + f(5) + f(7) + f(11) = 2 + 1 + 4 + 2 + 0 = 9.
2. The second query comes l = 3, r = 12. You need to count f(3) + f(5) + f(7) + f(11) = 1 + 4 + 2 + 0 = 7.
3. The third query comes l = 4, r = 4. As this interval has no prime numbers, then the sum equals 0.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
