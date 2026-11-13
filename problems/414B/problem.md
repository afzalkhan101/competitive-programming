# 414B · Mashmokh and ACM

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">combinatorics</span><span class="practice-tag">dp</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/414/B) · Rating 1400

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Mashmokh's boss, Bimokh, didn't like Mashmokh. So he fired him. Mashmokh decided to go to university and participate in ACM instead of finding a new job. He wants to become a member of Bamokh's team. In order to join he was given some programming tasks and one week to solve them. Mashmokh is not a very experienced programmer. Actually he is not a programmer at all. So he wasn't able to solve them. That's why he asked you to help him with these tasks. One of these tasks is the following.

A sequence of l integers b1, b2, ..., bl (1 ≤ b1 ≤ b2 ≤ ... ≤ bl ≤ n) is called good if each number divides (without a remainder) by the next number in the sequence. More formally $$b_{i} \mid b_{i+1}$$ for all i (1 ≤ i ≤ l - 1).

Given n and k find the number of good sequences of length k. As the answer can be rather large print it modulo 1000000007 (109 + 7).

## Input

The first line of input contains two space-separated integers n, k (1 ≤ n, k ≤ 2000).

## Output

Output a single integer — the number of good sequences of length k modulo 1000000007 (109 + 7).

## Sample 1

Input

```text
3 2
```

Output

```text
5
```

## Sample 2

Input

```text
6 4
```

Output

```text
39
```

## Sample 3

Input

```text
2 1
```

Output

```text
2
```

## Note

In the first sample the good sequences are: [1, 1], [2, 2], [3, 3], [1, 2], [1, 3].

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
