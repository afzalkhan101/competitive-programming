# 22D · Segments

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/22/D) · Rating 1900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

You are given n segments on the Ox-axis. You can drive a nail in any integer point on the Ox-axis line nail so, that all segments containing this point, are considered nailed down. If the nail passes through endpoint of some segment, this segment is considered to be nailed too. What is the smallest number of nails needed to nail all the segments down?

## Input

The first line of the input contains single integer number n (1 ≤ n ≤ 1000) — amount of segments. Following n lines contain descriptions of the segments. Each description is a pair of integer numbers — endpoints coordinates. All the coordinates don't exceed 10000 by absolute value. Segments can degenarate to points.

## Output

The first line should contain one integer number — the smallest number of nails needed to nail all the segments down. The second line should contain coordinates of driven nails separated by space in any order. If the answer is not unique, output any.

## Sample 1

Input

```text
2
0 2
2 5
```

Output

```text
1
2
```

## Sample 2

Input

```text
5
0 3
4 2
4 8
8 10
7 7
```

Output

```text
3
7 10 3
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
