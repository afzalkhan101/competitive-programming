# 52B · Right Triangles

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">combinatorics</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/52/B) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given a n × m field consisting only of periods ('.') and asterisks ('*'). Your task is to count all right triangles with two sides parallel to the square sides, whose vertices are in the centers of '*'-cells. A right triangle is a triangle in which one angle is a right angle (that is, a 90 degree angle).

## Input

The first line contains two positive integer numbers n and m (1 ≤ n, m ≤ 1000). The following n lines consist of m characters each, describing the field. Only '.' and '*' are allowed.

## Output

Output a single number — total number of square triangles in the field. Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d).

## Sample 1

Input

```text
2 2
**
*.
```

Output

```text
1
```

## Sample 2

Input

```text
3 4
*..*
.**.
*.**
```

Output

```text
9
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
