# 265B · Roadside Trees (Simplified Edition)

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/265/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Squirrel Liss loves nuts. There are n trees (numbered 1 to n from west to east) along a street and there is a delicious nut on the top of each tree. The height of the tree i is hi. Liss wants to eat all nuts.

Now Liss is on the root of the tree with the number 1. In one second Liss can perform one of the following actions:

- Walk up or down one unit on a tree.
- Eat a nut on the top of the current tree.
- Jump to the next tree. In this action the height of Liss doesn't change. More formally, when Liss is at height h of the tree i (1 ≤ i ≤ n - 1), she jumps to height h of the tree i + 1. This action can't be performed if h > hi + 1.

Compute the minimal time (in seconds) required to eat all nuts.

## Input

The first line contains an integer n (1  ≤  n ≤ 105) — the number of trees.

Next n lines contains the height of trees: i-th line contains an integer hi (1 ≤ hi ≤ 104) — the height of the tree with the number i.

## Output

Print a single integer — the minimal time required to eat all nuts in seconds.

## Sample 1

Input

```text
2
1
2
```

Output

```text
5
```

## Sample 2

Input

```text
5
2
1
2
1
1
```

Output

```text
14
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
