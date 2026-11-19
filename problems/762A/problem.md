<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 762A · k-th divisor

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/762/A) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given two integers n and k. Find k-th smallest divisor of n, or report that it doesn't exist.

Divisor of n is any such natural number, that n can be divided by it without remainder.

## Input

The first line contains two integers n and k (1 ≤ n ≤ 1015, 1 ≤ k ≤ 109).

## Output

If n has less than k divisors, output -1.

Otherwise, output the k-th smallest divisor of n.

## Sample 1

Input

```text
4 2
```

Output

```text
2
```

## Sample 2

Input

```text
5 3
```

Output

```text
-1
```

## Sample 3

Input

```text
12 5
```

Output

```text
6
```

## Note

In the first example, number 4 has three divisors: 1, 2 and 4. The second one is 2.

In the second example, number 5 has only two divisors: 1 and 5. The third divisor doesn't exist, so the answer is -1.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
