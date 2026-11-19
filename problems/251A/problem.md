<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 251A · Points on Line

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">binary search</span><span class="practice-tag">combinatorics</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/251/A) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Little Petya likes points a lot. Recently his mom has presented him n points lying on the line OX. Now Petya is wondering in how many ways he can choose three distinct points so that the distance between the two farthest of them doesn't exceed d.

Note that the order of the points inside the group of three chosen points doesn't matter.

## Input

The first line contains two integers: n and d (1 ≤ n ≤ 105; 1 ≤ d ≤ 109). The next line contains n integers x1, x2, ..., xn, their absolute value doesn't exceed 109 — the x-coordinates of the points that Petya has got.

It is guaranteed that the coordinates of the points in the input strictly increase.

## Output

Print a single integer — the number of groups of three points, where the distance between two farthest points doesn't exceed d.

Please do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.

## Sample 1

Input

```text
4 3
1 2 3 4
```

Output

```text
4
```

## Sample 2

Input

```text
4 2
-3 -2 -1 0
```

Output

```text
2
```

## Sample 3

Input

```text
5 19
1 10 20 30 50
```

Output

```text
1
```

## Note

In the first sample any group of three points meets our conditions.

In the seconds sample only 2 groups of three points meet our conditions: {-3, -2, -1} and {-2, -1, 0}.

In the third sample only one group does: {1, 10, 20}.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
