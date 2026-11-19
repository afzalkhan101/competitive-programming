<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 14C · Four Segments

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">geometry</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/14/C) · Rating 1700

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

Several months later Alex finally got his brother Bob's creation by post. And now, in his turn, Alex wants to boast about something to his brother. He thought for a while, and came to the conclusion that he has no ready creations, and decided to write a program for rectangles detection. According to his plan, the program detects if the four given segments form a rectangle of a positive area and with sides parallel to coordinate axes. As Alex does badly at school and can't write this program by himself, he asks you to help him.

## Input

The input data contain four lines. Each of these lines contains four integers x1, y1, x2, y2 ( - 109 ≤ x1, y1, x2, y2 ≤ 109) — coordinates of segment's beginning and end positions. The given segments can degenerate into points.

## Output

Output the word «YES», if the given four segments form the required rectangle, otherwise output «NO».

## Sample 1

Input

```text
1 1 6 1
1 0 6 0
6 0 6 1
1 1 1 0
```

Output

```text
YES
```

## Sample 2

Input

```text
0 0 0 3
2 0 0 0
2 2 2 0
0 2 2 2
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
