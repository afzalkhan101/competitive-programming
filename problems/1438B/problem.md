<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 1438B · Valerii Against Everyone

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">data structures</span><span class="practice-tag">greedy</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1438/B) · Rating 1000

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

You're given an array $$$b$$$ of length $$$n$$$. Let's define another array $$$a$$$, also of length $$$n$$$, for which $$$a_i = 2^{b_i}$$$ ($$$1 \leq i \leq n$$$).

Valerii says that every two non-intersecting subarrays of $$$a$$$ have different sums of elements. You want to determine if he is wrong. More formally, you need to determine if there exist four integers $$$l_1,r_1,l_2,r_2$$$ that satisfy the following conditions:

If such four integers exist, you will prove Valerii wrong. Do they exist?

An array $$$c$$$ is a subarray of an array $$$d$$$ if $$$c$$$ can be obtained from $$$d$$$ by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

## Input

Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 100$$$). Description of the test cases follows.

The first line of every test case contains a single integer $$$n$$$ ($$$2 \le n \le 1000$$$).

The second line of every test case contains $$$n$$$ integers $$$b_1,b_2,\ldots,b_n$$$ ($$$0 \le b_i \le 10^9$$$).

## Output

For every test case, if there exist two non-intersecting subarrays in $$$a$$$ that have the same sum, output YES on a separate line. Otherwise, output NO on a separate line.

Also, note that each letter can be in any case.

## Sample 1

Input

```text
2
6
4 3 0 1 2 0
2
2 5
```

Output

```text
YES
NO
```

## Note

In the first case, $$$a = [16,8,1,2,4,1]$$$. Choosing $$$l_1 = 1$$$, $$$r_1 = 1$$$, $$$l_2 = 2$$$ and $$$r_2 = 6$$$ works because $$$16 = (8+1+2+4+1)$$$.

In the second case, you can verify that there is no way to select to such subarrays.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
