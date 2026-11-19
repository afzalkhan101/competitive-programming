<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 81B · Sequence Formatting

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/81/B) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Polycarp is very careful. He even types numeric sequences carefully, unlike his classmates. If he sees a sequence without a space after the comma, with two spaces in a row, or when something else does not look neat, he rushes to correct it. For example, number sequence written like "1,2 ,3,...,   10" will be corrected to "1, 2, 3, ..., 10".

In this task you are given a string s, which is composed by a concatination of terms, each of which may be:

- a positive integer of an arbitrary length (leading zeroes are not allowed),
- a "comma" symbol (","),
- a "space" symbol (" "),
- "three dots" ("...", that is, exactly three points written one after another, also known as suspension points).

Polycarp wants to add and remove spaces in the string s to ensure the following:

- each comma is followed by exactly one space (if the comma is the last character in the string, this rule does not apply to it),
- each "three dots" term is preceded by exactly one space (if the dots are at the beginning of the string, this rule does not apply to the term),
- if two consecutive numbers were separated by spaces only (one or more), then exactly one of them should be left,
- there should not be other spaces.

Automate Polycarp's work and write a program that will process the given string s.

## Input

The input data contains a single string s. Its length is from 1 to 255 characters. The string s does not begin and end with a space. Its content matches the description given above.

## Output

Print the string s after it is processed. Your program's output should be exactly the same as the expected answer. It is permissible to end output line with a line-break character, and without it.

## Sample 1

Input

```text
1,2 ,3,...,     10
```

Output

```text
1, 2, 3, ..., 10
```

## Sample 2

Input

```text
1,,,4...5......6
```

Output

```text
1, , , 4 ...5 ... ...6
```

## Sample 3

Input

```text
...,1,2,3,...
```

Output

```text
..., 1, 2, 3, ...
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
