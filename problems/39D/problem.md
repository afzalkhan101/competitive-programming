# 39D · Cubical Planet

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/39/D) · Rating 1100

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

You can find anything whatsoever in our Galaxy! A cubical planet goes round an icosahedral star. Let us introduce a system of axes so that the edges of the cubical planet are parallel to the coordinate axes and two opposite vertices lay in the points (0, 0, 0) and (1, 1, 1). Two flies live on the planet. At the moment they are sitting on two different vertices of the cubical planet. Your task is to determine whether they see each other or not. The flies see each other when the vertices they occupy lie on the same face of the cube.

## Input

The first line contains three space-separated integers (0 or 1) — the coordinates of the first fly, the second line analogously contains the coordinates of the second fly.

## Output

Output "YES" (without quotes) if the flies see each other. Otherwise, output "NO".

## Sample 1

Input

```text
0 0 0
0 1 0
```

Output

```text
YES
```

## Sample 2

Input

```text
1 1 0
0 1 0
```

Output

```text
YES
```

## Sample 3

Input

```text
0 0 0
1 1 1
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
