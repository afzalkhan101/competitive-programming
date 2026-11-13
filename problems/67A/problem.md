# 67A · Partial Teacher

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dp</span><span class="practice-tag">graphs</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/67/A) · Rating 1800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

A teacher decides to give toffees to his students. He asks n students to stand in a queue. Since the teacher is very partial, he follows the following rule to distribute toffees.

He looks at the first two students and gives more toffees to the student having higher marks than the other one. If they have the same marks they get the same number of toffees. The same procedure is followed for each pair of adjacent students starting from the first one to the last one.

It is given that each student receives at least one toffee. You have to find the number of toffees given to each student by the teacher such that the total number of toffees is minimum.

## Input

The first line of input contains the number of students n (2 ≤ n ≤ 1000). The second line gives (n - 1) characters consisting of "L", "R" and "=". For each pair of adjacent students "L" means that the left student has higher marks, "R" means that the right student has higher marks and "=" means that both have equal marks.

## Output

Output consists of n integers separated by a space representing the number of toffees each student receives in the queue starting from the first one to the last one.

## Sample 1

Input

```text
5
LRLR
```

Output

```text
2 1 2 1 2
```

## Sample 2

Input

```text
5
=RRR
```

Output

```text
1 1 2 3 4
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
