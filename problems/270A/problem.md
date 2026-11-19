<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 270A · Fancy Fence

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">geometry</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/270/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Emuskald needs a fence around his farm, but he is too lazy to build it himself. So he purchased a fence-building robot.

He wants the fence to be a regular polygon. The robot builds the fence along a single path, but it can only make fence corners at a single angle a.

Will the robot be able to build the fence Emuskald wants? In other words, is there a regular polygon which angles are equal to a?

## Input

The first line of input contains an integer t (0 < t < 180) — the number of tests. Each of the following t lines contains a single integer a (0 < a < 180) — the angle the robot can make corners at measured in degrees.

## Output

For each test, output on a single line "YES" (without quotes), if the robot can build a fence Emuskald wants, and "NO" (without quotes), if it is impossible.

## Sample 1

Input

```text
3
30
60
90
```

Output

```text
NO
YES
YES
```

## Note

In the first test case, it is impossible to build the fence, since there is no regular polygon with angle $$30^\circ$$.

In the second test case, the fence is a regular triangle, and in the last test case — a square.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
