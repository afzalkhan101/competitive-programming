<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 31D · Chocolate

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/31/D) · Rating 2000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Bob has a rectangular chocolate bar of the size W × H. He introduced a cartesian coordinate system so that the point (0, 0) corresponds to the lower-left corner of the bar, and the point (W, H) corresponds to the upper-right corner. Bob decided to split the bar into pieces by breaking it. Each break is a segment parallel to one of the coordinate axes, which connects the edges of the bar. More formally, each break goes along the line x = xc or y = yc, where xc and yc are integers. It should divide one part of the bar into two non-empty parts. After Bob breaks some part into two parts, he breaks the resulting parts separately and independently from each other. Also he doesn't move the parts of the bar. Bob made n breaks and wrote them down in his notebook in arbitrary order. At the end he got n + 1 parts. Now he wants to calculate their areas. Bob is lazy, so he asks you to do this task.

## Input

The first line contains 3 integers W, H and n (1 ≤ W, H, n ≤ 100) — width of the bar, height of the bar and amount of breaks. Each of the following n lines contains four integers xi, 1, yi, 1, xi, 2, yi, 2 — coordinates of the endpoints of the i-th break (0 ≤ xi, 1 ≤ xi, 2 ≤ W, 0 ≤ yi, 1 ≤ yi, 2 ≤ H, or xi, 1 = xi, 2, or yi, 1 = yi, 2). Breaks are given in arbitrary order.

It is guaranteed that the set of breaks is correct, i.e. there is some order of the given breaks that each next break divides exactly one part of the bar into two non-empty parts.

## Output

Output n + 1 numbers — areas of the resulting parts in the increasing order.

## Sample 1

Input

```text
2 2 2
1 0 1 2
0 1 1 1
```

Output

```text
1 1 2
```

## Sample 2

Input

```text
2 2 3
1 0 1 2
0 1 1 1
1 1 2 1
```

Output

```text
1 1 1 1
```

## Sample 3

Input

```text
2 4 2
0 1 2 1
0 3 2 3
```

Output

```text
2 2 4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
