# 92A · Chips

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/92/A) · Rating 800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

There are n walruses sitting in a circle. All of them are numbered in the clockwise order: the walrus number 2 sits to the left of the walrus number 1, the walrus number 3 sits to the left of the walrus number 2, ..., the walrus number 1 sits to the left of the walrus number n.

The presenter has m chips. The presenter stands in the middle of the circle and starts giving the chips to the walruses starting from walrus number 1 and moving clockwise. The walrus number i gets i chips. If the presenter can't give the current walrus the required number of chips, then the presenter takes the remaining chips and the process ends. Determine by the given n and m how many chips the presenter will get in the end.

## Input

The first line contains two integers n and m (1 ≤ n ≤ 50, 1 ≤ m ≤ 104) — the number of walruses and the number of chips correspondingly.

## Output

Print the number of chips the presenter ended up with.

## Sample 1

Input

```text
4 11
```

Output

```text
0
```

## Sample 2

Input

```text
17 107
```

Output

```text
2
```

## Sample 3

Input

```text
3 8
```

Output

```text
1
```

## Note

In the first sample the presenter gives one chip to the walrus number 1, two chips to the walrus number 2, three chips to the walrus number 3, four chips to the walrus number 4, then again one chip to the walrus number 1. After that the presenter runs out of chips. He can't give anything to the walrus number 2 and the process finishes.

In the third sample the presenter gives one chip to the walrus number 1, two chips to the walrus number 2, three chips to the walrus number 3, then again one chip to the walrus number 1. The presenter has one chip left and he can't give two chips to the walrus number 2, that's why the presenter takes the last chip.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
