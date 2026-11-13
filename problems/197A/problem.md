# 197A · Plate Game

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">games</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/197/A) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You've got a rectangular table with length a and width b and the infinite number of plates of radius r. Two players play the following game: they take turns to put the plates on the table so that the plates don't lie on each other (but they can touch each other), and so that any point on any plate is located within the table's border. During the game one cannot move the plates that already lie on the table. The player who cannot make another move loses. Determine which player wins, the one who moves first or the one who moves second, provided that both players play optimally well.

## Input

A single line contains three space-separated integers a, b, r (1 ≤ a, b, r ≤ 100) — the table sides and the plates' radius, correspondingly.

## Output

If wins the player who moves first, print "First" (without the quotes). Otherwise print "Second" (without the quotes).

## Sample 1

Input

```text
5 5 2
```

Output

```text
First
```

## Sample 2

Input

```text
6 7 4
```

Output

```text
Second
```

## Note

In the first sample the table has place for only one plate. The first player puts a plate on the table, the second player can't do that and loses.

In the second sample the table is so small that it doesn't have enough place even for one plate. So the first player loses without making a single move.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
