# 217A · Ice Skating

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">dsu</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/217/A) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Bajtek is learning to skate on ice. He's a beginner, so his only mode of transportation is pushing off from a snow drift to the north, east, south or west and sliding until he lands in another snow drift. He has noticed that in this way it's impossible to get from some snow drifts to some other by any sequence of moves. He now wants to heap up some additional snow drifts, so that he can get from any snow drift to any other one. He asked you to find the minimal number of snow drifts that need to be created.

We assume that Bajtek can only heap up snow drifts at integer coordinates.

## Input

The first line of input contains a single integer n (1 ≤ n ≤ 100) — the number of snow drifts. Each of the following n lines contains two integers xi and yi (1 ≤ xi, yi ≤ 1000) — the coordinates of the i-th snow drift.

Note that the north direction coinсides with the direction of Oy axis, so the east direction coinсides with the direction of the Ox axis. All snow drift's locations are distinct.

## Output

Output the minimal number of snow drifts that need to be created in order for Bajtek to be able to reach any snow drift from any other one.

## Sample 1

Input

```text
2
2 1
1 2
```

Output

```text
1
```

## Sample 2

Input

```text
2
2 1
4 1
```

Output

```text
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
