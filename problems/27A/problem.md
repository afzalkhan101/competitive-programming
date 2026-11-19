<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 27A · Next Test

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">implementation</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/27/A) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

«Polygon» is a system which allows to create programming tasks in a simple and professional way. When you add a test to the problem, the corresponding form asks you for the test index. As in most cases it is clear which index the next test will have, the system suggests the default value of the index. It is calculated as the smallest positive integer which is not used as an index for some previously added test.

You are to implement this feature. Create a program which determines the default index of the next test, given the indexes of the previously added tests.

## Input

The first line contains one integer n (1 ≤ n ≤ 3000) — the amount of previously added tests. The second line contains n distinct integers a1, a2, ..., an (1 ≤ ai ≤ 3000) — indexes of these tests.

## Output

Output the required default value for the next test index.

## Sample 1

Input

```text
3
1 7 2
```

Output

```text
3
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
