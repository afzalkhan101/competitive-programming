# 60A · Where Are My Flakes?

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">implementation</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/60/A) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One morning the Cereal Guy found out that all his cereal flakes were gone. He found a note instead of them. It turned out that his smart roommate hid the flakes in one of n boxes. The boxes stand in one row, they are numbered from 1 to n from the left to the right. The roommate left hints like "Hidden to the left of the i-th box" ("To the left of i"), "Hidden to the right of the i-th box" ("To the right of i"). Such hints mean that there are no flakes in the i-th box as well. The Cereal Guy wants to know the minimal number of boxes he necessarily needs to check to find the flakes considering all the hints. Or he wants to find out that the hints are contradictory and the roommate lied to him, that is, no box has the flakes.

## Input

The first line contains two integers n and m (1 ≤ n ≤ 1000, 0 ≤ m ≤ 1000) which represent the number of boxes and the number of hints correspondingly. Next m lines contain hints like "To the left of i" and "To the right of i", where i is integer (1 ≤ i ≤ n). The hints may coincide.

## Output

The answer should contain exactly one integer — the number of boxes that should necessarily be checked or "-1" if the hints are contradictory.

## Sample 1

Input

```text
2 1
To the left of 2
```

Output

```text
1
```

## Sample 2

Input

```text
3 2
To the right of 1
To the right of 2
```

Output

```text
1
```

## Sample 3

Input

```text
3 1
To the left of 3
```

Output

```text
2
```

## Sample 4

Input

```text
3 2
To the left of 2
To the right of 1
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
