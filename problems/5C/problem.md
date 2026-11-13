# 5C · Longest Regular Bracket Sequence

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">data structures</span><span class="practice-tag">dp</span><span class="practice-tag">greedy</span><span class="practice-tag">sortings</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/5/C) · Rating 1900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

This is yet another problem dealing with regular bracket sequences.

We should remind you that a bracket sequence is called regular, if by inserting «+» and «1» into it we can get a correct mathematical expression. For example, sequences «(())()», «()» and «(()(()))» are regular, while «)(», «(()» and «(()))(» are not.

You are given a string of «(» and «)» characters. You are to find its longest substring that is a regular bracket sequence. You are to find the number of such substrings as well.

## Input

The first line of the input file contains a non-empty string, consisting of «(» and «)» characters. Its length does not exceed 106.

## Output

Print the length of the longest substring that is a regular bracket sequence, and the number of such substrings. If there are no such substrings, write the only line containing "0 1".

## Sample 1

Input

```text
)((())))(()())
```

Output

```text
6 2
```

## Sample 2

Input

```text
))(
```

Output

```text
0 1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
