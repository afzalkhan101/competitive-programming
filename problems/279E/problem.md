<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 279E · Beautiful Decomposition

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">dp</span><span class="practice-tag">games</span><span class="practice-tag">greedy</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/279/E) · Rating 1900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Valera considers a number beautiful, if it equals 2k or -2k for some integer k (k ≥ 0). Recently, the math teacher asked Valera to represent number n as the sum of beautiful numbers. As Valera is really greedy, he wants to complete the task using as few beautiful numbers as possible.

Help Valera and find, how many numbers he is going to need. In other words, if you look at all decompositions of the number n into beautiful summands, you need to find the size of the decomposition which has the fewest summands.

## Input

The first line contains string s (1 ≤ |s| ≤ 106), that is the binary representation of number n without leading zeroes (n > 0).

## Output

Print a single integer — the minimum amount of beautiful numbers that give a total of n.

## Sample 1

Input

```text
10
```

Output

```text
1
```

## Sample 2

Input

```text
111
```

Output

```text
2
```

## Sample 3

Input

```text
1101101
```

Output

```text
4
```

## Note

In the first sample n = 2 is a beautiful number.

In the second sample n = 7 and Valera can decompose it into sum 23 + ( - 20).

In the third sample n = 109 can be decomposed into the sum of four summands as follows: 27 + ( - 24) + ( - 22) + 20.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
