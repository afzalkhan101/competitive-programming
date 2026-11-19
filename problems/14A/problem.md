<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 14A · Letter

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/14/A) · Rating 800

Time: 1.0 seconds · Memory: 64.0 MB

## Problem

A boy Bob likes to draw. Not long ago he bought a rectangular graph (checked) sheet with n rows and m columns. Bob shaded some of the squares on the sheet. Having seen his masterpiece, he decided to share it with his elder brother, who lives in Flatland. Now Bob has to send his picture by post, but because of the world economic crisis and high oil prices, he wants to send his creation, but to spend as little money as possible. For each sent square of paper (no matter whether it is shaded or not) Bob has to pay 3.14 burles. Please, help Bob cut out of his masterpiece a rectangle of the minimum cost, that will contain all the shaded squares. The rectangle's sides should be parallel to the sheet's sides.

## Input

The first line of the input data contains numbers n and m (1 ≤ n, m ≤ 50), n — amount of lines, and m — amount of columns on Bob's sheet. The following n lines contain m characters each. Character «.» stands for a non-shaded square on the sheet, and «*» — for a shaded square. It is guaranteed that Bob has shaded at least one square.

## Output

Output the required rectangle of the minimum cost. Study the output data in the sample tests to understand the output format better.

## Sample 1

Input

```text
6 7
.......
..***..
..*....
..***..
..*....
..***..
```

Output

```text
***
*..
***
*..
***
```

## Sample 2

Input

```text
3 3
***
*.*
***
```

Output

```text
***
*.*
***
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
