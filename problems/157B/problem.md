# 157B · Trace

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">geometry</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/157/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One day, as Sherlock Holmes was tracking down one very important criminal, he found a wonderful painting on the wall. This wall could be represented as a plane. The painting had several concentric circles that divided the wall into several parts. Some parts were painted red and all the other were painted blue. Besides, any two neighboring parts were painted different colors, that is, the red and the blue color were alternating, i. e. followed one after the other. The outer area of the wall (the area that lied outside all circles) was painted blue. Help Sherlock Holmes determine the total area of red parts of the wall.

Let us remind you that two circles are called concentric if their centers coincide. Several circles are called concentric if any two of them are concentric.

## Input

The first line contains the single integer n (1 ≤ n ≤ 100). The second line contains n space-separated integers ri (1 ≤ ri ≤ 1000) — the circles' radii. It is guaranteed that all circles are different.

## Output

Print the single real number — total area of the part of the wall that is painted red. The answer is accepted if absolute or relative error doesn't exceed 10 - 4.

## Sample 1

Input

```text
1
1
```

Output

```text
3.1415926536
```

## Sample 2

Input

```text
3
1 4 2
```

Output

```text
40.8407044967
```

## Note

In the first sample the picture is just one circle of radius 1. Inner part of the circle is painted red. The area of the red part equals π × 12 = π.

In the second sample there are three circles of radii 1, 4 and 2. Outside part of the second circle is painted blue. Part between the second and the third circles is painted red. Part between the first and the third is painted blue. And, finally, the inner part of the first circle is painted red. Overall there are two red parts: the ring between the second and the third circles and the inner part of the first circle. Total area of the red parts is equal (π × 42 - π × 22) + π × 12 = π × 12 + π = 13π

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
