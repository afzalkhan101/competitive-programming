<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 6B · President's Office

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/6/B) · Rating 1100

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

President of Berland has a very vast office-room, where, apart from him, work his subordinates. Each subordinate, as well as President himself, has his own desk of a unique colour. Each desk is rectangular, and its sides are parallel to the office walls. One day President decided to establish an assembly, of which all his deputies will be members. Unfortunately, he does not remember the exact amount of his deputies, but he remembers that the desk of each his deputy is adjacent to his own desk, that is to say, the two desks (President's and each deputy's) have a common side of a positive length.

The office-room plan can be viewed as a matrix with n rows and m columns. Each cell of this matrix is either empty, or contains a part of a desk. An uppercase Latin letter stands for each desk colour. The «period» character («.») stands for an empty cell.

## Input

The first line contains two separated by a space integer numbers n, m (1 ≤ n, m ≤ 100) — the length and the width of the office-room, and c character — the President's desk colour. The following n lines contain m characters each — the office-room description. It is guaranteed that the colour of each desk is unique, and each desk represents a continuous subrectangle of the given matrix. All colours are marked by uppercase Latin letters.

## Output

Print the only number — the amount of President's deputies.

## Sample 1

Input

```text
3 4 R
G.B.
.RR.
TTT.
```

Output

```text
2
```

## Sample 2

Input

```text
3 3 Z
...
.H.
..Z
```

Output

```text
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
