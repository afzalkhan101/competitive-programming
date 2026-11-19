<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 313C · Ilya and Matrix

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/313/C) · Rating 1400

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Ilya is a very good-natured lion. He likes maths. Of all mathematical objects, his favourite one is matrices. Now he's faced a complicated matrix problem he needs to solve.

He's got a square 2n × 2n-sized matrix and 4n integers. You need to arrange all these numbers in the matrix (put each number in a single individual cell) so that the beauty of the resulting matrix with numbers is maximum.

The beauty of a 2n × 2n-sized matrix is an integer, obtained by the following algorithm:

1. Find the maximum element in the matrix. Let's denote it as m.
2. If n = 0, then the beauty of the matrix equals m. Otherwise, a matrix can be split into 4 non-intersecting 2n - 1 × 2n - 1-sized submatrices, then the beauty of the matrix equals the sum of number m and other four beauties of the described submatrices.

As you can see, the algorithm is recursive.

Help Ilya, solve the problem and print the resulting maximum beauty of the matrix.

## Input

The first line contains integer 4n (1 ≤ 4n ≤ 2·106). The next line contains 4n integers ai (1 ≤ ai ≤ 109) — the numbers you need to arrange in the 2n × 2n-sized matrix.

## Output

On a single line print the maximum value of the beauty of the described matrix.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.

## Sample 1

Input

```text
1
13
```

Output

```text
13
```

## Sample 2

Input

```text
4
1 2 3 4
```

Output

```text
14
```

## Note

Consider the second sample. You need to arrange the numbers in the matrix as follows:

Then the beauty of the matrix will equal: 4 + 1 + 2 + 3 + 4 = 14.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
