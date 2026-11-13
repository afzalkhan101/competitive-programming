# 135B · Rectangle and Square

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">geometry</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/135/B) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Little Petya very much likes rectangles and especially squares. Recently he has received 8 points on the plane as a gift from his mother. The points are pairwise distinct. Petya decided to split them into two sets each containing 4 points so that the points from the first set lay at the vertexes of some square and the points from the second set lay at the vertexes of a rectangle. Each point of initial 8 should belong to exactly one set. It is acceptable for a rectangle from the second set was also a square. If there are several partitions, Petya will be satisfied by any of them. Help him find such partition. Note that the rectangle and the square from the partition should have non-zero areas. The sides of the figures do not have to be parallel to the coordinate axes, though it might be the case.

## Input

You are given 8 pairs of integers, a pair per line — the coordinates of the points Petya has. The absolute value of all coordinates does not exceed 104. It is guaranteed that no two points coincide.

## Output

Print in the first output line "YES" (without the quotes), if the desired partition exists. In the second line output 4 space-separated numbers — point indexes from the input, which lie at the vertexes of the square. The points are numbered starting from 1. The numbers can be printed in any order. In the third line print the indexes of points lying at the vertexes of a rectangle in the similar format. All printed numbers should be pairwise distinct.

If the required partition does not exist, the first line should contain the word "NO" (without the quotes), after which no output is needed.

## Sample 1

Input

```text
0 0
10 11
10 0
0 11
1 1
2 2
2 1
1 2
```

Output

```text
YES
5 6 7 8
1 2 3 4
```

## Sample 2

Input

```text
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
```

Output

```text
NO
```

## Sample 3

Input

```text
0 0
4 4
4 0
0 4
1 2
2 3
3 2
2 1
```

Output

```text
YES
1 2 3 4
5 6 7 8
```

## Note

Pay attention to the third example: the figures do not necessarily have to be parallel to the coordinate axes.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
