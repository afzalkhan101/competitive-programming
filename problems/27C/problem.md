# 27C · Unordered Subsequence

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/27/C) · Rating 1900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The sequence is called ordered if it is non-decreasing or non-increasing. For example, sequnces [3, 1, 1, 0] and [1, 2, 3, 100] are ordered, but the sequence [1, 3, 3, 1] is not. You are given a sequence of numbers. You are to find it's shortest subsequence which is not ordered.

A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

## Input

The first line of the input contains one integer n (1 ≤ n ≤ 105). The second line contains n space-separated integers — the given sequence. All numbers in this sequence do not exceed 106 by absolute value.

## Output

If the given sequence does not contain any unordered subsequences, output 0. Otherwise, output the length k of the shortest such subsequence. Then output k integers from the range [1..n] — indexes of the elements of this subsequence. If there are several solutions, output any of them.

## Sample 1

Input

```text
5
67 499 600 42 23
```

Output

```text
3
1 3 5
```

## Sample 2

Input

```text
3
1 2 3
```

Output

```text
0
```

## Sample 3

Input

```text
3
2 3 1
```

Output

```text
3
1 2 3
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
