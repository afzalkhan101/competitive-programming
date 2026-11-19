<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 59E · Shortest Path

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">graphs</span><span class="practice-tag">shortest paths</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/59/E) · Rating 2000

Time: 3.0 seconds · Memory: 256.0 MB

## Problem

In Ancient Berland there were n cities and m two-way roads of equal length. The cities are numbered with integers from 1 to n inclusively. According to an ancient superstition, if a traveller visits three cities ai, bi, ci in row, without visiting other cities between them, a great disaster awaits him. Overall there are k such city triplets. Each triplet is ordered, which means that, for example, you are allowed to visit the cities in the following order: ai, ci, bi. Vasya wants to get from the city 1 to the city n and not fulfil the superstition. Find out which minimal number of roads he should take. Also you are required to find one of his possible path routes.

## Input

The first line contains three integers n, m, k (2 ≤ n ≤ 3000, 1 ≤ m ≤ 20000, 0 ≤ k ≤ 105) which are the number of cities, the number of roads and the number of the forbidden triplets correspondingly.

Then follow m lines each containing two integers xi, yi (1 ≤ xi, yi ≤ n) which are the road descriptions. The road is described by the numbers of the cities it joins. No road joins a city with itself, there cannot be more than one road between a pair of cities.

Then follow k lines each containing three integers ai, bi, ci (1 ≤ ai, bi, ci ≤ n) which are the forbidden triplets. Each ordered triplet is listed mo more than one time. All three cities in each triplet are distinct.

City n can be unreachable from city 1 by roads.

## Output

If there are no path from 1 to n print -1. Otherwise on the first line print the number of roads d along the shortest path from the city 1 to the city n. On the second line print d + 1 numbers — any of the possible shortest paths for Vasya. The path should start in the city 1 and end in the city n.

## Sample 1

Input

```text
4 4 1
1 2
2 3
3 4
1 3
1 4 3
```

Output

```text
2
1 3 4
```

## Sample 2

Input

```text
3 1 0
1 2
```

Output

```text
-1
```

## Sample 3

Input

```text
4 4 2
1 2
2 3
3 4
1 3
1 2 3
1 3 4
```

Output

```text
4
1 3 2 3 4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
