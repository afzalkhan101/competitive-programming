# 34D · Road Map

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/34/D) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

There are n cities in Berland. Each city has its index — an integer number from 1 to n. The capital has index r1. All the roads in Berland are two-way. The road system is such that there is exactly one path from the capital to each city, i.e. the road map looks like a tree. In Berland's chronicles the road map is kept in the following way: for each city i, different from the capital, there is kept number pi — index of the last city on the way from the capital to i.

Once the king of Berland Berl XXXIV decided to move the capital from city r1 to city r2. Naturally, after this the old representation of the road map in Berland's chronicles became incorrect. Please, help the king find out a new representation of the road map in the way described above.

## Input

The first line contains three space-separated integers n, r1, r2 (2 ≤ n ≤ 5·104, 1 ≤ r1 ≠ r2 ≤ n) — amount of cities in Berland, index of the old capital and index of the new one, correspondingly.

The following line contains n - 1 space-separated integers — the old representation of the road map. For each city, apart from r1, there is given integer pi — index of the last city on the way from the capital to city i. All the cities are described in order of increasing indexes.

## Output

Output n - 1 numbers — new representation of the road map in the same format.

## Sample 1

Input

```text
3 2 3
2 2
```

Output

```text
2 3
```

## Sample 2

Input

```text
6 2 4
6 1 2 4 2
```

Output

```text
6 4 1 4 2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
