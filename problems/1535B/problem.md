<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 1535B · Array Reodering

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">greedy</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1535/B) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given an array $$$a$$$ consisting of $$$n$$$ integers.

Let's call a pair of indices $$$i$$$, $$$j$$$ good if $$$1 \le i < j \le n$$$ and $$$\gcd(a_i, 2a_j) > 1$$$ (where $$$\gcd(x, y)$$$ is the greatest common divisor of $$$x$$$ and $$$y$$$).

Find the maximum number of good index pairs if you can reorder the array $$$a$$$ in an arbitrary way.

## Input

The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.

The first line of the test case contains a single integer $$$n$$$ ($$$2 \le n \le 2000$$$) — the number of elements in the array.

The second line of the test case contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 10^5$$$).

It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2000$$$.

## Output

For each test case, output a single integer — the maximum number of good index pairs if you can reorder the array $$$a$$$ in an arbitrary way.

## Sample 1

Input

```text
3
4
3 6 5 3
2
1 7
5
1 4 2 4 1
```

Output

```text
4
0
9
```

## Note

In the first example, the array elements can be rearranged as follows: $$$[6, 3, 5, 3]$$$.

In the third example, the array elements can be rearranged as follows: $$$[4, 4, 2, 1, 1]$$$.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
