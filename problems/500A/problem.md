<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 500A · New Year Transportation

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/500/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

New Year is coming in Line World! In this world, there are n cells numbered by integers from 1 to n, as a 1 × n board. People live in cells. However, it was hard to move between distinct cells, because of the difficulty of escaping the cell. People wanted to meet people who live in other cells.

So, user tncks0121 has made a transportation system to move between these cells, to celebrate the New Year. First, he thought of n - 1 positive integers a1, a2, ..., an - 1. For every integer i where 1 ≤ i ≤ n - 1 the condition 1 ≤ ai ≤ n - i holds. Next, he made n - 1 portals, numbered by integers from 1 to n - 1. The i-th (1 ≤ i ≤ n - 1) portal connects cell i and cell (i + ai), and one can travel from cell i to cell (i + ai) using the i-th portal. Unfortunately, one cannot use the portal backwards, which means one cannot move from cell (i + ai) to cell i using the i-th portal. It is easy to see that because of condition 1 ≤ ai ≤ n - i one can't leave the Line World using portals.

Currently, I am standing at cell 1, and I want to go to cell t. However, I don't know whether it is possible to go there. Please determine whether I can go to cell t by only using the construted transportation system.

## Input

The first line contains two space-separated integers n (3 ≤ n ≤ 3 × 104) and t (2 ≤ t ≤ n) — the number of cells, and the index of the cell which I want to go to.

The second line contains n - 1 space-separated integers a1, a2, ..., an - 1 (1 ≤ ai ≤ n - i). It is guaranteed, that using the given transportation system, one cannot leave the Line World.

## Output

If I can go to cell t using the transportation system, print "YES". Otherwise, print "NO".

## Sample 1

Input

```text
8 4
1 2 1 2 1 2 1
```

Output

```text
YES
```

## Sample 2

Input

```text
8 5
1 2 1 2 1 1 1
```

Output

```text
NO
```

## Note

In the first sample, the visited cells are: 1, 2, 4; so we can successfully visit the cell 4.

In the second sample, the possible cells to visit are: 1, 2, 4, 6, 7, 8; so we can't visit the cell 5, which we want to visit.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
