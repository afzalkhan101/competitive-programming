# 24C · Sequence of points

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">geometry</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/24/C) · Rating 1800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given the following points with integer coordinates on the plane: M0, A0, A1, ..., An - 1, where n is odd number. Now we define the following infinite sequence of points Mi: Mi is symmetric to Mi - 1 according $${ A } _ { ( i - 1 ) \mod n }$$ (for every natural number i). Here point B is symmetric to A according M, if M is the center of the line segment AB. Given index j find the point Mj.

## Input

On the first line you will be given an integer n (1 ≤ n ≤ 105), which will be odd, and j (1 ≤ j ≤ 1018), where j is the index of the desired point. The next line contains two space separated integers, the coordinates of M0. After that n lines follow, where the i-th line contain the space separated integer coordinates of the point Ai - 1. The absolute values of all input coordinates will not be greater then 1000.

## Output

On a single line output the coordinates of Mj, space separated.

## Sample 1

Input

```text
3 4
0 0
1 1
2 3
-5 3
```

Output

```text
14 0
```

## Sample 2

Input

```text
3 1
5 5
1000 1000
-1000 1000
3 100
```

Output

```text
1995 1995
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
