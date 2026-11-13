# 600B · Queries about less or equal elements

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">binary search</span><span class="practice-tag">data structures</span><span class="practice-tag">sortings</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/600/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given two arrays of integers a and b. For each element of the second array bj you should find the number of elements in array a that are less than or equal to the value bj.

## Input

The first line contains two integers n, m (1 ≤ n, m ≤ 2·105) — the sizes of arrays a and b.

The second line contains n integers — the elements of array a ( - 109 ≤ ai ≤ 109).

The third line contains m integers — the elements of array b ( - 109 ≤ bj ≤ 109).

## Output

Print m integers, separated by spaces: the j-th of which is equal to the number of such elements in array a that are less than or equal to the value bj.

## Sample 1

Input

```text
5 4
1 3 5 7 9
6 4 2 8
```

Output

```text
3 2 1 4
```

## Sample 2

Input

```text
5 5
1 2 1 2 5
3 1 4 1 5
```

Output

```text
4 2 4 2 5
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
