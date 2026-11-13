# 244A · Dividing Orange

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/244/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One day Ms Swan bought an orange in a shop. The orange consisted of n·k segments, numbered with integers from 1 to n·k.

There were k children waiting for Ms Swan at home. The children have recently learned about the orange and they decided to divide it between them. For that each child took a piece of paper and wrote the number of the segment that he would like to get: the i-th (1 ≤ i ≤ k) child wrote the number ai (1 ≤ ai ≤ n·k). All numbers ai accidentally turned out to be different.

Now the children wonder, how to divide the orange so as to meet these conditions:

- each child gets exactly n orange segments;
- the i-th child gets the segment with number ai for sure;
- no segment goes to two children simultaneously.

Help the children, divide the orange and fulfill the requirements, described above.

## Input

The first line contains two integers n, k (1 ≤ n, k ≤ 30). The second line contains k space-separated integers a1, a2, ..., ak (1 ≤ ai ≤ n·k), where ai is the number of the orange segment that the i-th child would like to get.

It is guaranteed that all numbers ai are distinct.

## Output

Print exactly n·k distinct integers. The first n integers represent the indexes of the segments the first child will get, the second n integers represent the indexes of the segments the second child will get, and so on. Separate the printed numbers with whitespaces.

You can print a child's segment indexes in any order. It is guaranteed that the answer always exists. If there are multiple correct answers, print any of them.

## Sample 1

Input

```text
2 2
4 1
```

Output

```text
2 4
1 3
```

## Sample 2

Input

```text
3 1
2
```

Output

```text
3 2 1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
