# 264A · Escape from Stones

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">data structures</span><span class="practice-tag">implementation</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/264/A) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Squirrel Liss lived in a forest peacefully, but unexpected trouble happens. Stones fall from a mountain. Initially Squirrel Liss occupies an interval [0, 1]. Next, n stones will fall and Liss will escape from the stones. The stones are numbered from 1 to n in order.

The stones always fall to the center of Liss's interval. When Liss occupies the interval [k - d, k + d] and a stone falls to k, she will escape to the left or to the right. If she escapes to the left, her new interval will be [k - d, k]. If she escapes to the right, her new interval will be [k, k + d].

You are given a string s of length n. If the i-th character of s is "l" or "r", when the i-th stone falls Liss will escape to the left or to the right, respectively. Find the sequence of stones' numbers from left to right after all the n stones falls.

## Input

The input consists of only one line. The only line contains the string s (1 ≤ |s| ≤ 106). Each character in s will be either "l" or "r".

## Output

Output n lines — on the i-th line you should print the i-th stone's number from the left.

## Sample 1

Input

```text
llrlr
```

Output

```text
3
5
4
2
1
```

## Sample 2

Input

```text
rrlll
```

Output

```text
1
2
5
4
3
```

## Sample 3

Input

```text
lrlrr
```

Output

```text
2
4
5
3
1
```

## Note

In the first example, the positions of stones 1, 2, 3, 4, 5 will be $$\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{3}{16}, \frac{5}{32}$$, respectively. So you should print the sequence: 3, 5, 4, 2, 1.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
