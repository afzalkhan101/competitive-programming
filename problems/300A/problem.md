<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 300A · Array

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/300/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vitaly has an array of n distinct integers. Vitaly wants to divide this array into three non-empty sets so as the following conditions hold:

1. The product of all numbers in the first set is less than zero ( < 0).
2. The product of all numbers in the second set is greater than zero ( > 0).
3. The product of all numbers in the third set is equal to zero.
4. Each number from the initial array must occur in exactly one set.

Help Vitaly. Divide the given array.

## Input

The first line of the input contains integer n (3 ≤ n ≤ 100). The second line contains n space-separated distinct integers a1, a2, ..., an (|ai| ≤ 103) — the array elements.

## Output

In the first line print integer n1 (n1 > 0) — the number of elements in the first set. Then print n1 numbers — the elements that got to the first set.

In the next line print integer n2 (n2 > 0) — the number of elements in the second set. Then print n2 numbers — the elements that got to the second set.

In the next line print integer n3 (n3 > 0) — the number of elements in the third set. Then print n3 numbers — the elements that got to the third set.

The printed sets must meet the described conditions. It is guaranteed that the solution exists. If there are several solutions, you are allowed to print any of them.

## Sample 1

Input

```text
3
-1 2 0
```

Output

```text
1 -1
1 2
1 0
```

## Sample 2

Input

```text
4
-1 -2 -3 0
```

Output

```text
1 -1
2 -3 -2
1 0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
