<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 14B · Young Photographer

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/14/B) · Rating 1000

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

Among other things, Bob is keen on photography. Especially he likes to take pictures of sportsmen. That was the reason why he placed himself in position x0 of a long straight racetrack and got ready to take pictures. But the problem was that not all the runners passed him. The total amount of sportsmen, training at that racetrack, equals n. And each of them regularly runs distances within a particular segment of the racetrack, which is the same for each sportsman. For example, the first sportsman runs from position a1 to position b1, the second — from a2 to b2

What is the minimum distance that Bob should move to have a chance to take pictures of each sportsman? Bob can take a picture of a sportsman, if he stands within the segment that this sportsman covers on the racetrack.

## Input

The first line of the input file contains integers n and x0 (1 ≤ n ≤ 100; 0 ≤ x0 ≤ 1000). The following n lines contain pairs of integers ai, bi (0 ≤ ai, bi ≤ 1000; ai ≠ bi).

## Output

Output the required minimum distance in the same units as the positions on the racetrack. If there is no such a position, output -1.

## Sample 1

Input

```text
3 3
0 7
14 2
4 6
```

Output

```text
1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
