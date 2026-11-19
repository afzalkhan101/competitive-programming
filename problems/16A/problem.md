<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 16A · Flag

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/16/A) · Rating 800

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

According to a new ISO standard, a flag of every country should have a chequered field n × m, each square should be of one of 10 colours, and the flag should be «striped»: each horizontal row of the flag should contain squares of the same colour, and the colours of adjacent horizontal rows should be different. Berland's government asked you to find out whether their flag meets the new ISO standard.

## Input

The first line of the input contains numbers n and m (1 ≤ n, m ≤ 100), n — the amount of rows, m — the amount of columns on the flag of Berland. Then there follows the description of the flag: each of the following n lines contain m characters. Each character is a digit between 0 and 9, and stands for the colour of the corresponding square.

## Output

Output YES, if the flag meets the new ISO standard, and NO otherwise.

## Sample 1

Input

```text
3 3
000
111
222
```

Output

```text
YES
```

## Sample 2

Input

```text
3 3
000
000
111
```

Output

```text
NO
```

## Sample 3

Input

```text
3 3
000
111
002
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
