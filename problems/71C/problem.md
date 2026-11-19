<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 71C · Round Table Knights

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">dp</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/71/C) · Rating 1600

Time: 0.5 seconds · Memory: 256.0 MB

## Problem

There are n knights sitting at the Round Table at an equal distance from each other. Each of them is either in a good or in a bad mood.

Merlin, the wizard predicted to King Arthur that the next month will turn out to be particularly fortunate if the regular polygon can be found. On all vertices of the polygon knights in a good mood should be located. Otherwise, the next month will bring misfortunes.

A convex polygon is regular if all its sides have same length and all his angles are equal. In this problem we consider only regular polygons with at least 3 vertices, i. e. only nondegenerated.

On a picture below some examples of such polygons are present. Green points mean knights in a good mood. Red points mean ones in a bad mood.

King Arthur knows the knights' moods. Help him find out if the next month will be fortunate or not.

## Input

The first line contains number n, which is the number of knights at the round table (3 ≤ n ≤ 105). The second line contains space-separated moods of all the n knights in the order of passing them around the table. "1" means that the knight is in a good mood an "0" means that he is in a bad mood.

## Output

Print "YES" without the quotes if the following month will turn out to be lucky. Otherwise, print "NO".

## Sample 1

Input

```text
3
1 1 1
```

Output

```text
YES
```

## Sample 2

Input

```text
6
1 0 1 1 1 0
```

Output

```text
YES
```

## Sample 3

Input

```text
6
1 0 0 1 0 1
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
