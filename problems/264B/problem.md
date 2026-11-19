<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 264B · Good Sequences

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">dp</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/264/B) · Rating 1500

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Squirrel Liss is interested in sequences. She also has preferences of integers. She thinks n integers a1, a2, ..., an are good.

Now she is interested in good sequences. A sequence x1, x2, ..., xk is called good if it satisfies the following three conditions:

- The sequence is strictly increasing, i.e. xi < xi + 1 for each i (1 ≤ i ≤ k - 1).
- No two adjacent elements are coprime, i.e. gcd(xi, xi + 1) > 1 for each i (1 ≤ i ≤ k - 1) (where gcd(p, q) denotes the greatest common divisor of the integers p and q).
- All elements of the sequence are good integers.

Find the length of the longest good sequence.

## Input

The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 105) — the number of good integers. The second line contains a single-space separated list of good integers a1, a2, ..., an in strictly increasing order (1 ≤ ai ≤ 105; ai < ai + 1).

## Output

Print a single integer — the length of the longest good sequence.

## Sample 1

Input

```text
5
2 3 4 6 9
```

Output

```text
4
```

## Sample 2

Input

```text
9
1 2 3 5 6 7 8 9 10
```

Output

```text
4
```

## Note

In the first example, the following sequences are examples of good sequences: [2; 4; 6; 9], [2; 4; 6], [3; 9], [6]. The length of the longest good sequence is 4.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
