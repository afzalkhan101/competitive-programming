# 75C · Modified GCD

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">binary search</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/75/C) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Well, here is another math class task. In mathematics, GCD is the greatest common divisor, and it's an easy task to calculate the GCD between two positive integers.

A common divisor for two positive numbers is a number which both numbers are divisible by.

But your teacher wants to give you a harder task, in this task you have to find the greatest common divisor d between two integers a and b that is in a given range from low to high (inclusive), i.e. low ≤ d ≤ high. It is possible that there is no common divisor in the given range.

You will be given the two integers a and b, then n queries. Each query is a range from low to high and you have to answer each query.

## Input

The first line contains two integers a and b, the two integers as described above (1 ≤ a, b ≤ 109). The second line contains one integer n, the number of queries (1 ≤ n ≤ 104). Then n lines follow, each line contains one query consisting of two integers, low and high (1 ≤ low ≤ high ≤ 109).

## Output

Print n lines. The i-th of them should contain the result of the i-th query in the input. If there is no common divisor in the given range for any query, you should print -1 as a result for this query.

## Sample 1

Input

```text
9 27
3
1 5
10 11
9 11
```

Output

```text
3
-1
9
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
