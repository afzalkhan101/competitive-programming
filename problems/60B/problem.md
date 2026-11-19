<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 60B · Serial Time!

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">dsu</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/60/B) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The Cereal Guy's friend Serial Guy likes to watch soap operas. An episode is about to start, and he hasn't washed his plate yet. But he decided to at least put in under the tap to be filled with water. The plate can be represented by a parallelepiped k × n × m, that is, it has k layers (the first layer is the upper one), each of which is a rectangle n × m with empty squares ('.') and obstacles ('#'). The water can only be present in the empty squares. The tap is positioned above the square (x, y) of the first layer, it is guaranteed that this square is empty. Every minute a cubical unit of water falls into the plate. Find out in how many minutes the Serial Guy should unglue himself from the soap opera and turn the water off for it not to overfill the plate. That is, you should find the moment of time when the plate is absolutely full and is going to be overfilled in the next moment.

Note: the water fills all the area within reach (see sample 4). Water flows in each of the 6 directions, through faces of 1 × 1 × 1 cubes.

## Input

The first line contains three numbers k, n, m (1 ≤ k, n, m ≤ 10) which are the sizes of the plate. Then follow k rectangles consisting of n lines each containing m characters '.' or '#', which represents the "layers" of the plate in the order from the top to the bottom. The rectangles are separated by empty lines (see the samples). The last line contains x and y (1 ≤ x ≤ n, 1 ≤ y ≤ m) which are the tap's coordinates. x is the number of the line and y is the number of the column. Lines of each layer are numbered from left to right by the integers from 1 to n, columns of each layer are numbered from top to bottom by the integers from 1 to m.

## Output

The answer should contain a single number, showing in how many minutes the plate will be filled.

## Sample 1

Input

```text
1 1 1
.
1 1
```

Output

```text
1
```

## Sample 2

Input

```text
2 1 1
.
#
1 1
```

Output

```text
1
```

## Sample 3

Input

```text
2 2 2
.#
##
..
..
1 1
```

Output

```text
5
```

## Sample 4

Input

```text
3 2 2
#.
##
#.
.#
..
..
1 2
```

Output

```text
7
```

## Sample 5

Input

```text
3 3 3
.#.
###
##.
.##
###
##.
...
...
...
1 1
```

Output

```text
13
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
