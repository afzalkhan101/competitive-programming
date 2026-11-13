# 616A · Comparing Two Long Integers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/616/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You are given two very long integers a, b (leading zeroes are allowed). You should check what number a or b is greater or determine that they are equal.

The input size is very large so don't use the reading of symbols one by one. Instead of that use the reading of a whole line or token.

As input/output can reach huge size it is recommended to use fast input/output methods: for example, prefer to use scanf/printf instead of cin/cout in C++, prefer to use BufferedReader/PrintWriter instead of Scanner/System.out in Java. Don't use the function input() in Python2 instead of it use the function raw_input().

## Input

The first line contains a non-negative integer a.

The second line contains a non-negative integer b.

The numbers a, b may contain leading zeroes. Each of them contains no more than 106 digits.

## Output

Print the symbol "<" if a < b and the symbol ">" if a > b. If the numbers are equal print the symbol "=".

## Sample 1

Input

```text
9
10
```

Output

```text
<
```

## Sample 2

Input

```text
11
10
```

Output

```text
>
```

## Sample 3

Input

```text
00012345
12345
```

Output

```text
=
```

## Sample 4

Input

```text
0123
9
```

Output

```text
>
```

## Sample 5

Input

```text
0123
111
```

Output

```text
>
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
