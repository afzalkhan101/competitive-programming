<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 141B · Hopscotch

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">geometry</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/141/B) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

So nearly half of the winter is over and Maria is dreaming about summer. She's fed up with skates and sleds, she was dreaming about Hopscotch all night long. It's a very popular children's game. The game field, the court, looks as is shown in the figure (all blocks are square and are numbered from bottom to top, blocks in the same row are numbered from left to right). Let us describe the hopscotch with numbers that denote the number of squares in the row, staring from the lowest one: 1-1-2-1-2-1-2-(1-2)..., where then the period is repeated (1-2).

The coordinate system is defined as shown in the figure. Side of all the squares are equal and have length a.

Maria is a very smart and clever girl, and she is concerned with quite serious issues: if she throws a stone into a point with coordinates (x, y), then will she hit some square? If the answer is positive, you are also required to determine the number of the square.

It is believed that the stone has fallen into the square if it is located strictly inside it. In other words a stone that has fallen on the square border is not considered a to hit a square.

## Input

The only input line contains three integers: a, x, y, where a (1 ≤ a ≤ 100) is the side of the square, x and y ( - 106 ≤ x ≤ 106, 0 ≤ y ≤ 106) are coordinates of the stone.

## Output

Print the number of the square, inside which the stone fell. If the stone is on a border of some stone or outside the court, print "-1" without the quotes.

## Sample 1

Input

```text
1 0 0
```

Output

```text
-1
```

## Sample 2

Input

```text
3 1 1
```

Output

```text
1
```

## Sample 3

Input

```text
3 0 10
```

Output

```text
5
```

## Sample 4

Input

```text
3 0 7
```

Output

```text
-1
```

## Sample 5

Input

```text
3 4 0
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
