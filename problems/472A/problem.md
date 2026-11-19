<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 472A · Design Tutorial: Learn from Math

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/472/A) · Rating 800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

One way to create a task is to learn from math. You can generate some random math statement or modify some theorems to get something new and build a new task from that.

For example, there is a statement called the "Goldbach's conjecture". It says: "each even number no less than four can be expressed as the sum of two primes". Let's modify it. How about a statement like that: "each integer no less than 12 can be expressed as the sum of two composite numbers." Not like the Goldbach's conjecture, I can prove this theorem.

You are given an integer n no less than 12, express it as a sum of two composite numbers.

## Input

The only line contains an integer n (12 ≤ n ≤ 106).

## Output

Output two composite integers x and y (1 < x, y < n) such that x + y = n. If there are multiple solutions, you can output any of them.

## Sample 1

Input

```text
12
```

Output

```text
4 8
```

## Sample 2

Input

```text
15
```

Output

```text
6 9
```

## Sample 3

Input

```text
23
```

Output

```text
8 15
```

## Sample 4

Input

```text
1000000
```

Output

```text
500000 500000
```

## Note

In the first example, 12 = 4 + 8 and both 4, 8 are composite numbers. You can output "6 6" or "8 4" as well.

In the second example, 15 = 6 + 9. Note that you can't output "1 14" because 1 is not a composite number.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
