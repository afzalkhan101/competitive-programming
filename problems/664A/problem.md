<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 664A · Complicated GCD

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/664/A) · Rating 800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Greatest common divisor GCD(a, b) of two positive integers a and b is equal to the biggest integer d such that both integers a and b are divisible by d. There are many efficient algorithms to find greatest common divisor GCD(a, b), for example, Euclid algorithm.

Formally, find the biggest integer d, such that all integers a, a + 1, a + 2, ..., b are divisible by d. To make the problem even more complicated we allow a and b to be up to googol, 10100 — such number do not fit even in 64-bit integer type!

## Input

The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10100).

## Output

Output one integer — greatest common divisor of all integers from a to b inclusive.

## Sample 1

Input

```text
1 2
```

Output

```text
1
```

## Sample 2

Input

```text
61803398874989484820458683436563811772030917980576 61803398874989484820458683436563811772030917980576
```

Output

```text
61803398874989484820458683436563811772030917980576
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
