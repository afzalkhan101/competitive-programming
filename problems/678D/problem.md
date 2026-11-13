# 678D · Iterated Linear Function

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/678/D) · Rating 1700

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Consider a linear function f(x) = Ax + B. Let's define g(0)(x) = x and g(n)(x) = f(g(n - 1)(x)) for n > 0. For the given integer values A, B, n and x find the value of g(n)(x) modulo 109 + 7.

## Input

The only line contains four integers A, B, n and x (1 ≤ A, B, x ≤ 109, 1 ≤ n ≤ 1018) — the parameters from the problem statement.

Note that the given value n can be too large, so you should use 64-bit integer type to store it. In C++ you can use the long long integer type and in Java you can use long integer type.

## Output

Print the only integer s — the value g(n)(x) modulo 109 + 7.

## Sample 1

Input

```text
3 4 1 1
```

Output

```text
7
```

## Sample 2

Input

```text
3 4 2 1
```

Output

```text
25
```

## Sample 3

Input

```text
3 4 3 1
```

Output

```text
79
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
