# 45I · TCMCF+++

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/45/I) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya has gotten interested in programming contests in TCMCF+++ rules. On the contest n problems were suggested and every problem had a cost — a certain integral number of points (perhaps, negative or even equal to zero). According to TCMCF+++ rules, only accepted problems can earn points and the overall number of points of a contestant was equal to the product of the costs of all the problems he/she had completed. If a person didn't solve anything, then he/she didn't even appear in final standings and wasn't considered as participant. Vasya understood that to get the maximal number of points it is not always useful to solve all the problems. Unfortunately, he understood it only after the contest was finished. Now he asks you to help him: find out what problems he had to solve to earn the maximal number of points.

## Input

The first line contains an integer n (1 ≤ n ≤ 100) — the number of the suggested problems. The next line contains n space-separated integers ci ( - 100 ≤ ci ≤ 100) — the cost of the i-th task. The tasks' costs may coinсide.

## Output

Print space-separated the costs of the problems that needed to be solved to get the maximal possible number of points. Do not forget, please, that it was necessary to solve at least one problem. If there are several solutions to that problem, print any of them.

## Sample 1

Input

```text
5
1 2 -3 3 3
```

Output

```text
3 1 2 3
```

## Sample 2

Input

```text
13
100 100 100 100 100 100 100 100 100 100 100 100 100
```

Output

```text
100 100 100 100 100 100 100 100 100 100 100 100 100
```

## Sample 3

Input

```text
4
-2 -2 -2 -2
```

Output

```text
-2 -2 -2 -2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
