<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 369A · Valera and Plates

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/369/A) · Rating 900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Valera is a lazy student. He has m clean bowls and k clean plates.

Valera has made an eating plan for the next n days. As Valera is lazy, he will eat exactly one dish per day. At that, in order to eat a dish, he needs exactly one clean plate or bowl. We know that Valera can cook only two types of dishes. He can eat dishes of the first type from bowls and dishes of the second type from either bowls or plates.

When Valera finishes eating, he leaves a dirty plate/bowl behind. His life philosophy doesn't let him eat from dirty kitchenware. So sometimes he needs to wash his plate/bowl before eating. Find the minimum number of times Valera will need to wash a plate/bowl, if he acts optimally.

## Input

The first line of the input contains three integers n, m, k (1 ≤ n, m, k ≤ 1000) — the number of the planned days, the number of clean bowls and the number of clean plates.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 2). If ai equals one, then on day i Valera will eat a first type dish. If ai equals two, then on day i Valera will eat a second type dish.

## Output

Print a single integer — the minimum number of times Valera will need to wash a plate/bowl.

## Sample 1

Input

```text
3 1 1
1 2 1
```

Output

```text
1
```

## Sample 2

Input

```text
4 3 1
1 1 1 1
```

Output

```text
1
```

## Sample 3

Input

```text
3 1 2
2 2 2
```

Output

```text
0
```

## Sample 4

Input

```text
8 2 2
1 2 1 2 1 2 1 2
```

Output

```text
4
```

## Note

In the first sample Valera will wash a bowl only on the third day, so the answer is one.

In the second sample, Valera will have the first type of the dish during all four days, and since there are only three bowls, he will wash a bowl exactly once.

In the third sample, Valera will have the second type of dish for all three days, and as they can be eaten from either a plate or a bowl, he will never need to wash a plate/bowl.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
