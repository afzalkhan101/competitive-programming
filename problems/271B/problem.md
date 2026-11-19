<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 271B · Prime Matrix

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">binary search</span><span class="practice-tag">brute force</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/271/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You've got an n × m matrix. The matrix consists of integers. In one move, you can apply a single transformation to the matrix: choose an arbitrary element of the matrix and increase it by 1. Each element can be increased an arbitrary number of times.

You are really curious about prime numbers. Let us remind you that a prime number is a positive integer that has exactly two distinct positive integer divisors: itself and number one. For example, numbers 2, 3, 5 are prime and numbers 1, 4, 6 are not.

A matrix is prime if at least one of the two following conditions fulfills:

- the matrix has a row with prime numbers only;
- the matrix has a column with prime numbers only;

Your task is to count the minimum number of moves needed to get a prime matrix from the one you've got.

## Input

The first line contains two integers n, m (1 ≤ n, m ≤ 500) — the number of rows and columns in the matrix, correspondingly.

Each of the following n lines contains m integers — the initial matrix. All matrix elements are positive integers. All numbers in the initial matrix do not exceed 105.

The numbers in the lines are separated by single spaces.

## Output

Print a single integer — the minimum number of moves needed to get a prime matrix from the one you've got. If you've got a prime matrix, print 0.

## Sample 1

Input

```text
3 3
1 2 3
5 6 1
4 4 1
```

Output

```text
1
```

## Sample 2

Input

```text
2 3
4 8 8
9 2 9
```

Output

```text
3
```

## Sample 3

Input

```text
2 2
1 3
4 2
```

Output

```text
0
```

## Note

In the first sample you need to increase number 1 in cell (1, 1). Thus, the first row will consist of prime numbers: 2, 2, 3.

In the second sample you need to increase number 8 in cell (1, 2) three times. Thus, the second column will consist of prime numbers: 11, 2.

In the third sample you don't have to do anything as the second column already consists of prime numbers: 3, 2.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
