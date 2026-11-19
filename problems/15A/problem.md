<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 15A · Cottage Village

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">implementation</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/15/A) · Rating 1200

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

A new cottage village called «Flatville» is being built in Flatland. By now they have already built in «Flatville» n square houses with the centres on the Оx-axis. The houses' sides are parallel to the coordinate axes. It's known that no two houses overlap, but they can touch each other.

The architect bureau, where Peter works, was commissioned to build a new house in «Flatville». The customer wants his future house to be on the Оx-axis, to be square in shape, have a side t, and touch at least one of the already built houses. For sure, its sides should be parallel to the coordinate axes, its centre should be on the Ox-axis and it shouldn't overlap any of the houses in the village.

Peter was given a list of all the houses in «Flatville». Would you help him find the amount of possible positions of the new house?

## Input

The first line of the input data contains numbers n and t (1 ≤ n, t ≤ 1000). Then there follow n lines, each of them contains two space-separated integer numbers: xi ai, where xi — x-coordinate of the centre of the i-th house, and ai — length of its side ( - 1000 ≤ xi ≤ 1000, 1 ≤ ai ≤ 1000).

## Output

Output the amount of possible positions of the new house.

## Sample 1

Input

```text
2 2
0 4
6 2
```

Output

```text
4
```

## Sample 2

Input

```text
2 2
0 4
5 2
```

Output

```text
3
```

## Sample 3

Input

```text
2 3
0 4
5 2
```

Output

```text
2
```

## Note

It is possible for the x-coordinate of the new house to have non-integer value.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
