<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 14D · Two Paths

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">dp</span><span class="practice-tag">graphs</span><span class="practice-tag">shortest paths</span><span class="practice-tag">trees</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/14/D) · Rating 1900

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

As you know, Bob's brother lives in Flatland. In Flatland there are n cities, connected by n - 1 two-way roads. The cities are numbered from 1 to n. You can get from one city to another moving along the roads.

The «Two Paths» company, where Bob's brother works, has won a tender to repair two paths in Flatland. A path is a sequence of different cities, connected sequentially by roads. The company is allowed to choose by itself the paths to repair. The only condition they have to meet is that the two paths shouldn't cross (i.e. shouldn't have common cities).

It is known that the profit, the «Two Paths» company will get, equals the product of the lengths of the two paths. Let's consider the length of each road equals 1, and the length of a path equals the amount of roads in it. Find the maximum possible profit for the company.

## Input

The first line contains an integer n (2 ≤ n ≤ 200), where n is the amount of cities in the country. The following n - 1 lines contain the information about the roads. Each line contains a pair of numbers of the cities, connected by the road ai, bi (1 ≤ ai, bi ≤ n).

## Output

Output the maximum possible profit.

## Sample 1

Input

```text
4
1 2
2 3
3 4
```

Output

```text
1
```

## Sample 2

Input

```text
7
1 2
1 3
1 4
1 5
1 6
1 7
```

Output

```text
0
```

## Sample 3

Input

```text
6
1 2
2 3
2 4
5 4
6 4
```

Output

```text
4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
