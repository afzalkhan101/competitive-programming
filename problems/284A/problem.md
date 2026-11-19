<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 284A · Cows and Primitive Roots

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/284/A) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The cows have just learned what a primitive root is! Given a prime p, a primitive root $$\bmod p$$ is an integer x (1 ≤ x < p) such that none of integers x - 1, x2 - 1, ..., xp - 2 - 1 are divisible by p, but xp - 1 - 1 is.

Unfortunately, computing primitive roots can be time consuming, so the cows need your help. Given a prime p, help the cows find the number of primitive roots $$\bmod p$$.

## Input

The input contains a single line containing an integer p (2 ≤ p < 2000). It is guaranteed that p is a prime.

## Output

Output on a single line the number of primitive roots $$\bmod p$$.

## Sample 1

Input

```text
3
```

Output

```text
1
```

## Sample 2

Input

```text
5
```

Output

```text
2
```

## Note

The only primitive root $$\bmod 3$$ is 2.

The primitive roots $$\bmod 5$$ are 2 and 3.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
