# 45J · Planting Trees

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/45/J) · Rating 1800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya is a Greencode wildlife preservation society proponent. One day he found an empty field nobody owned, divided it into n × m squares and decided to plant a forest there. Vasya will plant nm trees of all different heights from 1 to nm. For his forest to look more natural he wants any two trees growing in the side neighbouring squares to have the absolute value of difference in heights to be strictly more than 1. Help Vasya: make the plan of the forest planting for which this condition is fulfilled.

## Input

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 100) — the number of rows and columns on Vasya's field

## Output

If there's no solution, print -1. Otherwise, print n lines containing m numbers each — the trees' planting plan. In every square of the plan the height of a tree that should be planted on this square should be written. If there are several solutions to that problem, print any of them.

## Sample 1

Input

```text
2 3
```

Output

```text
3 6 2
5 1 4
```

## Sample 2

Input

```text
2 1
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
