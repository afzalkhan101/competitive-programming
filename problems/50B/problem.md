<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 50B · Choosing Symbol Pairs

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/50/B) · Rating 1500

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

There is a given string S consisting of N symbols. Your task is to find the number of ordered pairs of integers i and j such that

1. 1 ≤ i, j ≤ N

2. S[i] = S[j], that is the i-th symbol of string S is equal to the j-th.

## Input

The single input line contains S, consisting of lowercase Latin letters and digits. It is guaranteed that string S in not empty and its length does not exceed 105.

## Output

Print a single number which represents the number of pairs i and j with the needed property. Pairs (x, y) and (y, x) should be considered different, i.e. the ordered pairs count.

## Sample 1

Input

```text
great10
```

Output

```text
7
```

## Sample 2

Input

```text
aaaaaaaaaa
```

Output

```text
100
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
