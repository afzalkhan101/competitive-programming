# 336C · Vasily the Bear and Sequence

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/336/C) · Rating 1800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Vasily the bear has got a sequence of positive integers a1, a2, ..., an. Vasily the Bear wants to write out several numbers on a piece of paper so that the beauty of the numbers he wrote out was maximum.

The beauty of the written out numbers b1, b2, ..., bk is such maximum non-negative integer v, that number b1 and b2 and ... and bk is divisible by number 2v without a remainder. If such number v doesn't exist (that is, for any non-negative integer v, number b1 and b2 and ... and bk is divisible by 2v without a remainder), the beauty of the written out numbers equals -1.

Tell the bear which numbers he should write out so that the beauty of the written out numbers is maximum. If there are multiple ways to write out the numbers, you need to choose the one where the bear writes out as many numbers as possible.

Here expression x and y means applying the bitwise AND operation to numbers x and y. In programming languages C++ and Java this operation is represented by "&", in Pascal — by "and".

## Input

The first line contains integer n (1 ≤ n ≤ 105). The second line contains n space-separated integers a1, a2, ..., an (1 ≤ a1 < a2 < ... < an ≤ 109).

## Output

In the first line print a single integer k (k > 0), showing how many numbers to write out. In the second line print k integers b1, b2, ..., bk — the numbers to write out. You are allowed to print numbers b1, b2, ..., bk in any order, but all of them must be distinct. If there are multiple ways to write out the numbers, choose the one with the maximum number of numbers to write out. If there still are multiple ways, you are allowed to print any of them.

## Sample 1

Input

```text
5
1 2 3 4 5
```

Output

```text
2
4 5
```

## Sample 2

Input

```text
3
1 2 4
```

Output

```text
1
4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
