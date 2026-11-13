# 134B · Pairs of Numbers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/134/B) · Rating 1900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Let's assume that we have a pair of numbers (a, b). We can get a new pair (a + b, b) or (a, a + b) from the given pair in a single step.

Let the initial pair of numbers be (1,1). Your task is to find number k, that is, the least number of steps needed to transform (1,1) into the pair where at least one number equals n.

## Input

The input contains the only integer n (1 ≤ n ≤ 106).

## Output

Print the only integer k.

## Sample 1

Input

```text
5
```

Output

```text
3
```

## Sample 2

Input

```text
1
```

Output

```text
0
```

## Note

The pair (1,1) can be transformed into a pair containing 5 in three moves: (1,1)  →  (1,2)  →  (3,2)  →  (5,2).

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
