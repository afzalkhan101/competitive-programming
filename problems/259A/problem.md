<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 259A · Little Elephant and Chess

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/259/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The Little Elephant loves chess very much.

One day the Little Elephant and his friend decided to play chess. They've got the chess pieces but the board is a problem. They've got an 8 × 8 checkered board, each square is painted either black or white. The Little Elephant and his friend know that a proper chessboard doesn't have any side-adjacent cells with the same color and the upper left cell is white. To play chess, they want to make the board they have a proper chessboard. For that the friends can choose any row of the board and cyclically shift the cells of the chosen row, that is, put the last (rightmost) square on the first place in the row and shift the others one position to the right. You can run the described operation multiple times (or not run it at all).

For example, if the first line of the board looks like that "BBBBBBWW" (the white cells of the line are marked with character "W", the black cells are marked with character "B"), then after one cyclic shift it will look like that "WBBBBBBW".

Help the Little Elephant and his friend to find out whether they can use any number of the described operations to turn the board they have into a proper chessboard.

## Input

The input consists of exactly eight lines. Each line contains exactly eight characters "W" or "B" without any spaces: the j-th character in the i-th line stands for the color of the j-th cell of the i-th row of the elephants' board. Character "W" stands for the white color, character "B" stands for the black color.

Consider the rows of the board numbered from 1 to 8 from top to bottom, and the columns — from 1 to 8 from left to right. The given board can initially be a proper chessboard.

## Output

In a single line print "YES" (without the quotes), if we can make the board a proper chessboard and "NO" (without the quotes) otherwise.

## Sample 1

Input

```text
WBWBWBWB
BWBWBWBW
BWBWBWBW
BWBWBWBW
WBWBWBWB
WBWBWBWB
BWBWBWBW
WBWBWBWB
```

Output

```text
YES
```

## Sample 2

Input

```text
WBWBWBWB
WBWBWBWB
BBWBWWWB
BWBWBWBW
BWBWBWBW
BWBWBWWW
BWBWBWBW
BWBWBWBW
```

Output

```text
NO
```

## Note

In the first sample you should shift the following lines one position to the right: the 3-rd, the 6-th, the 7-th and the 8-th.

In the second sample there is no way you can achieve the goal.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
