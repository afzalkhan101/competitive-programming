# 330B · Road Construction

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/330/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

A country has n cities. Initially, there is no road in the country. One day, the king decides to construct some roads connecting pairs of cities. Roads can be traversed either way. He wants those roads to be constructed in such a way that it is possible to go from each city to any other city by traversing at most two roads. You are also given m pairs of cities — roads cannot be constructed between these pairs of cities.

Your task is to construct the minimum number of roads that still satisfy the above conditions. The constraints will guarantee that this is always possible.

## Input

The first line consists of two integers n and m $$( 1 \leq n \leq 1 0 ^ { 3 }, 0 \leq m < \frac { n } { 2 } )$$.

Then m lines follow, each consisting of two integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi), which means that it is not possible to construct a road connecting cities ai and bi. Consider the cities are numbered from 1 to n.

It is guaranteed that every pair of cities will appear at most once in the input.

## Output

You should print an integer s: the minimum number of roads that should be constructed, in the first line. Then s lines should follow, each consisting of two integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi), which means that a road should be constructed between cities ai and bi.

If there are several solutions, you may print any of them.

## Sample 1

Input

```text
4 1
1 3
```

Output

```text
3
1 2
4 2
2 3
```

## Note

This is one possible solution of the example:

These are examples of wrong solutions:

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
