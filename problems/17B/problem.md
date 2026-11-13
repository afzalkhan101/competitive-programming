# 17B · Hierarchy

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">dsu</span><span class="practice-tag">greedy</span><span class="practice-tag">shortest paths</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/17/B) · Rating 1500

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

Nick's company employed n people. Now Nick needs to build a tree hierarchy of «supervisor-surbodinate» relations in the company (this is to say that each employee, except one, has exactly one supervisor). There are m applications written in the following form: «employee ai is ready to become a supervisor of employee bi at extra cost ci». The qualification qj of each employee is known, and for each application the following is true: qai > qbi.

Would you help Nick calculate the minimum cost of such a hierarchy, or find out that it is impossible to build it.

## Input

The first input line contains integer n (1 ≤ n ≤ 1000) — amount of employees in the company. The following line contains n space-separated numbers qj (0 ≤ qj ≤ 106)— the employees' qualifications. The following line contains number m (0 ≤ m ≤ 10000) — amount of received applications. The following m lines contain the applications themselves, each of them in the form of three space-separated numbers: ai, bi and ci (1 ≤ ai, bi ≤ n, 0 ≤ ci ≤ 106). Different applications can be similar, i.e. they can come from one and the same employee who offered to become a supervisor of the same person but at a different cost. For each application qai > qbi.

## Output

Output the only line — the minimum cost of building such a hierarchy, or -1 if it is impossible to build it.

## Sample 1

Input

```text
4
7 2 3 1
4
1 2 5
2 4 1
3 4 1
1 3 5
```

Output

```text
11
```

## Sample 2

Input

```text
3
1 2 3
2
3 1 2
3 1 3
```

Output

```text
-1
```

## Note

In the first sample one of the possible ways for building a hierarchy is to take applications with indexes 1, 2 and 4, which give 11 as the minimum total cost. In the second sample it is impossible to build the required hierarchy, so the answer is -1.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
