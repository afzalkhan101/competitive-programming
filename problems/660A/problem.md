# 660A · Co-prime Array

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/660/A) · Rating 1200

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

You are given an array of n elements, you must make it a co-prime array in as few moves as possible.

In each move you can insert any positive integral number you want not greater than 109 in any place in the array.

An array is co-prime if any two adjacent numbers of it are co-prime.

In the number theory, two integers a and b are said to be co-prime if the only positive integer that divides both of them is 1.

## Input

The first line contains integer n (1 ≤ n ≤ 1000) — the number of elements in the given array.

The second line contains n integers ai (1 ≤ ai ≤ 109) — the elements of the array a.

## Output

Print integer k on the first line — the least number of elements needed to add to the array a to make it co-prime.

The second line should contain n + k integers aj — the elements of the array a after adding k elements to it. Note that the new array should be co-prime, so any two adjacent values should be co-prime. Also the new array should be got from the original array a by adding k elements to it.

If there are multiple answers you can print any one of them.

## Sample 1

Input

```text
3
2 7 28
```

Output

```text
1
2 7 9 28
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
