<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 25C · Roads in Berland

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">graphs</span><span class="practice-tag">shortest paths</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/25/C) · Rating 1900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

There are n cities numbered from 1 to n in Berland. Some of them are connected by two-way roads. Each road has its own length — an integer number from 1 to 1000. It is known that from each city it is possible to get to any other city by existing roads. Also for each pair of cities it is known the shortest distance between them. Berland Government plans to build k new roads. For each of the planned road it is known its length, and what cities it will connect. To control the correctness of the construction of new roads, after the opening of another road Berland government wants to check the sum of the shortest distances between all pairs of cities. Help them — for a given matrix of shortest distances on the old roads and plans of all new roads, find out how the sum of the shortest distances between all pairs of cities changes after construction of each road.

## Input

The first line contains integer n (2 ≤ n ≤ 300) — amount of cities in Berland. Then there follow n lines with n integer numbers each — the matrix of shortest distances. j-th integer in the i-th row — di, j, the shortest distance between cities i and j. It is guaranteed that di, i = 0, di, j = dj, i, and a given matrix is a matrix of shortest distances for some set of two-way roads with integer lengths from 1 to 1000, such that from each city it is possible to get to any other city using these roads.

Next line contains integer k (1 ≤ k ≤ 300) — amount of planned roads. Following k lines contain the description of the planned roads. Each road is described by three space-separated integers ai, bi, ci (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ci ≤ 1000) — ai and bi — pair of cities, which the road connects, ci — the length of the road. It can be several roads between a pair of cities, but no road connects the city with itself.

## Output

Output k space-separated integers qi (1 ≤ i ≤ k). qi should be equal to the sum of shortest distances between all pairs of cities after the construction of roads with indexes from 1 to i. Roads are numbered from 1 in the input order. Each pair of cities should be taken into account in the sum exactly once, i. e. we count unordered pairs.

## Sample 1

Input

```text
2
0 5
5 0
1
1 2 3
```

Output

```text
3
```

## Sample 2

Input

```text
3
0 4 5
4 0 9
5 9 0
2
2 3 8
1 2 1
```

Output

```text
17 12
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
