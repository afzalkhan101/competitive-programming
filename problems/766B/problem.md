<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 766B · Mahmoud and a Triangle

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">geometry</span><span class="practice-tag">greedy</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/766/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Mahmoud has n line segments, the i-th of them has length ai. Ehab challenged him to use exactly 3 line segments to form a non-degenerate triangle. Mahmoud doesn't accept challenges unless he is sure he can win, so he asked you to tell him if he should accept the challenge. Given the lengths of the line segments, check if he can choose exactly 3 of them to form a non-degenerate triangle.

Mahmoud should use exactly 3 line segments, he can't concatenate two line segments or change any length. A non-degenerate triangle is a triangle with positive area.

## Input

The first line contains single integer n (3 ≤ n ≤ 105) — the number of line segments Mahmoud has.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the lengths of line segments Mahmoud has.

## Output

In the only line print "YES" if he can choose exactly three line segments and form a non-degenerate triangle with them, and "NO" otherwise.

## Sample 1

Input

```text
5
1 5 3 2 4
```

Output

```text
YES
```

## Sample 2

Input

```text
3
4 1 2
```

Output

```text
NO
```

## Note

For the first example, he can use line segments with lengths 2, 4 and 5 to form a non-degenerate triangle.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
