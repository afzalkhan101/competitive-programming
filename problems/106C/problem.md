<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 106C · Buns

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">dp</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/106/C) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Lavrenty, a baker, is going to make several buns with stuffings and sell them.

Lavrenty has n grams of dough as well as m different stuffing types. The stuffing types are numerated from 1 to m. Lavrenty knows that he has ai grams left of the i-th stuffing. It takes exactly bi grams of stuffing i and ci grams of dough to cook a bun with the i-th stuffing. Such bun can be sold for di tugriks.

Also he can make buns without stuffings. Each of such buns requires c0 grams of dough and it can be sold for d0 tugriks. So Lavrenty can cook any number of buns with different stuffings or without it unless he runs out of dough and the stuffings. Lavrenty throws away all excess material left after baking.

Find the maximum number of tugriks Lavrenty can earn.

## Input

The first line contains 4 integers n, m, c0 and d0 (1 ≤ n ≤ 1000, 1 ≤ m ≤ 10, 1 ≤ c0, d0 ≤ 100). Each of the following m lines contains 4 integers. The i-th line contains numbers ai, bi, ci and di (1 ≤ ai, bi, ci, di ≤ 100).

## Output

Print the only number — the maximum number of tugriks Lavrenty can earn.

## Sample 1

Input

```text
10 2 2 1
7 3 2 100
12 3 1 10
```

Output

```text
241
```

## Sample 2

Input

```text
100 1 25 50
15 5 20 10
```

Output

```text
200
```

## Note

To get the maximum number of tugriks in the first sample, you need to cook 2 buns with stuffing 1, 4 buns with stuffing 2 and a bun without any stuffing.

In the second sample Lavrenty should cook 4 buns without stuffings.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
