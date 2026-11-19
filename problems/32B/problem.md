<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 32B · Borze

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">expression parsing</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/32/B) · Rating 800

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

## Input

The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

## Output

Output the decoded ternary number. It can have leading zeroes.

## Sample 1

Input

```text
.-.--
```

Output

```text
012
```

## Sample 2

Input

```text
--.
```

Output

```text
20
```

## Sample 3

Input

```text
-..-.--
```

Output

```text
1012
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
