<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 79C · Beaver

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">data structures</span><span class="practice-tag">dp</span><span class="practice-tag">greedy</span><span class="practice-tag">hashing</span><span class="practice-tag">strings</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/79/C) · Rating 1800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

After Fox Ciel got off a bus, she found that the bus she was on was a wrong bus and she lost her way in a strange town. However, she fortunately met her friend Beaver Taro and asked which way to go to her castle. Taro's response to her was a string s, and she tried to remember the string s correctly.

However, Ciel feels n strings b1, b2, ... , bn are really boring, and unfortunately she dislikes to remember a string that contains a boring substring. To make the thing worse, what she can remember is only the contiguous substring of s.

Determine the longest contiguous substring of s that does not contain any boring string, so that she can remember the longest part of Taro's response.

## Input

In the first line there is a string s. The length of s will be between 1 and 105, inclusive.

In the second line there is a single integer n (1 ≤ n ≤ 10).  Next n lines, there is a string bi (1 ≤ i ≤ n). Each length of bi will be between 1 and 10, inclusive.

Each character of the given strings will be either a English alphabet (both lowercase and uppercase) or a underscore ('_') or a digit. Assume that these strings are case-sensitive.

## Output

Output in the first line two space-separated integers len and pos: the length of the longest contiguous substring of s that does not contain any bi, and the first position of the substring (0-indexed). The position pos must be between 0 and |s| - len inclusive, where |s| is the length of string s.

If there are several solutions, output any.

## Sample 1

Input

```text
Go_straight_along_this_street
5
str
long
tree
biginteger
ellipse
```

Output

```text
12 4
```

## Sample 2

Input

```text
IhaveNoIdea
9
I
h
a
v
e
N
o
I
d
```

Output

```text
0 0
```

## Sample 3

Input

```text
unagioisii
2
ioi
unagi
```

Output

```text
5 5
```

## Note

In the first sample, the solution is traight_alon.

In the second sample, the solution is an empty string, so the output can be «0 0», «0 1», «0 2», and so on.

In the third sample, the solution is either nagio or oisii.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
