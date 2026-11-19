<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 776B · Sherlock and his girlfriend

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/776/B) · Rating 1200

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Sherlock has a new girlfriend (so unlike him!). Valentine's day is coming and he wants to gift her some jewelry.

He bought n pieces of jewelry. The i-th piece has price equal to i + 1, that is, the prices of the jewelry are 2, 3, 4, ... n + 1.

Watson gave Sherlock a challenge to color these jewelry pieces such that two pieces don't have the same color if the price of one piece is a prime divisor of the price of the other piece. Also, Watson asked him to minimize the number of different colors used.

Help Sherlock complete this trivial task.

## Input

The only line contains single integer n (1 ≤ n ≤ 100000) — the number of jewelry pieces.

## Output

The first line of output should contain a single integer k, the minimum number of colors that can be used to color the pieces of jewelry with the given constraints.

The next line should consist of n space-separated integers (between 1 and k) that specify the color of each piece in the order of increasing price.

If there are multiple ways to color the pieces using k colors, you can output any of them.

## Sample 1

Input

```text
3
```

Output

```text
2
1 1 2
```

## Sample 2

Input

```text
4
```

Output

```text
2
2 1 1 2
```

## Note

In the first input, the colors for first, second and third pieces of jewelry having respective prices 2, 3 and 4 are 1, 1 and 2 respectively.

In this case, as 2 is a prime divisor of 4, colors of jewelry having prices 2 and 4 must be distinct.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
