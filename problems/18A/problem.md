# 18A · Triangle

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">geometry</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/18/A) · Rating 1500

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

At a geometry lesson Bob learnt that a triangle is called right-angled if it is nondegenerate and one of its angles is right. Bob decided to draw such a triangle immediately: on a sheet of paper he drew three points with integer coordinates, and joined them with segments of straight lines, then he showed the triangle to Peter. Peter said that Bob's triangle is not right-angled, but is almost right-angled: the triangle itself is not right-angled, but it is possible to move one of the points exactly by distance 1 so, that all the coordinates remain integer, and the triangle become right-angled. Bob asks you to help him and find out if Peter tricks him. By the given coordinates of the triangle you should find out if it is right-angled, almost right-angled, or neither of these.

## Input

The first input line contains 6 space-separated integers x1, y1, x2, y2, x3, y3 — coordinates of the triangle's vertices. All the coordinates are integer and don't exceed 100 in absolute value. It's guaranteed that the triangle is nondegenerate, i.e. its total area is not zero.

## Output

If the given triangle is right-angled, output RIGHT, if it is almost right-angled, output ALMOST, and if it is neither of these, output NEITHER.

## Sample 1

Input

```text
0 0 2 0 0 1
```

Output

```text
RIGHT
```

## Sample 2

Input

```text
2 3 4 5 6 6
```

Output

```text
NEITHER
```

## Sample 3

Input

```text
-1 0 2 0 0 1
```

Output

```text
ALMOST
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
