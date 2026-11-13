# 124B · Permutations

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">combinatorics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/124/B) · Rating 1400

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

You are given n k-digit integers. You have to rearrange the digits in the integers so that the difference between the largest and the smallest number was minimum. Digits should be rearranged by the same rule in all integers.

## Input

The first line contains integers n and k — the number and digit capacity of numbers correspondingly (1 ≤ n, k ≤ 8). Next n lines contain k-digit positive integers. Leading zeroes are allowed both in the initial integers and the integers resulting from the rearranging of digits.

## Output

Print a single number: the minimally possible difference between the largest and the smallest number after the digits are rearranged in all integers by the same rule.

## Sample 1

Input

```text
6 4
5237
2753
7523
5723
5327
2537
```

Output

```text
2700
```

## Sample 2

Input

```text
3 3
010
909
012
```

Output

```text
3
```

## Sample 3

Input

```text
7 5
50808
36603
37198
44911
29994
42543
50156
```

Output

```text
20522
```

## Note

In the first sample, if we rearrange the digits in numbers as (3,1,4,2), then the 2-nd and the 4-th numbers will equal 5237 and 2537 correspondingly (they will be maximum and minimum for such order of digits).

In the second sample, if we swap the second digits and the first ones, we get integers 100, 99 and 102.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
