# 118B · Present from Lena

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/118/B) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya's birthday is approaching and Lena decided to sew a patterned handkerchief to him as a present. Lena chose digits from 0 to n as the pattern. The digits will form a rhombus. The largest digit n should be located in the centre. The digits should decrease as they approach the edges. For example, for n = 5 the handkerchief pattern should look like that:

Your task is to determine the way the handkerchief will look like by the given n.

## Input

The first line contains the single integer n (2 ≤ n ≤ 9).

## Output

Print a picture for the given n. You should strictly observe the number of spaces before the first digit on each line. Every two adjacent digits in the same line should be separated by exactly one space. There should be no spaces after the last digit at the end of each line.

## Sample 1

Input

```text
2
```

Output

```text
0
0 1 0
0 1 2 1 0
0 1 0
0
```

## Sample 2

Input

```text
3
```

Output

```text
0
0 1 0
0 1 2 1 0
0 1 2 3 2 1 0
0 1 2 1 0
0 1 0
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
