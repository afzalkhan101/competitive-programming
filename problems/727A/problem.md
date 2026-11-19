<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 727A · Transformation: from A to B

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/727/A) · Rating 1000

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Vasily has a number a, which he wants to turn into a number b. For this purpose, he can do two types of operations:

- multiply the current number by 2 (that is, replace the number x by 2·x);
- append the digit 1 to the right of current number (that is, replace the number x by 10·x + 1).

You need to help Vasily to transform the number a into the number b using only the operations described above, or find that it is impossible.

Note that in this task you are not required to minimize the number of operations. It suffices to find any way to transform a into b.

## Input

The first line contains two positive integers a and b (1 ≤ a < b ≤ 109) — the number which Vasily has and the number he wants to have.

## Output

If there is no way to get b from a, print "NO" (without quotes).

Otherwise print three lines. On the first line print "YES" (without quotes). The second line should contain single integer k — the length of the transformation sequence. On the third line print the sequence of transformations x1, x2, ..., xk, where:

- x1 should be equal to a,
- xk should be equal to b,
- xi should be obtained from xi - 1 using any of two described operations (1 < i ≤ k).

If there are multiple answers, print any of them.

## Sample 1

Input

```text
2 162
```

Output

```text
YES
5
2 4 8 81 162
```

## Sample 2

Input

```text
4 42
```

Output

```text
NO
```

## Sample 3

Input

```text
100 40021
```

Output

```text
YES
5
100 200 2001 4002 40021
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
