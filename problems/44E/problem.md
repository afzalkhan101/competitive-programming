<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 44E · Anfisa the Monkey

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">dp</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/44/E) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Anfisa the monkey learns to type. She is yet unfamiliar with the "space" key and can only type in lower-case Latin letters. Having typed for a fairly long line, Anfisa understood that it would be great to divide what she has written into k lines not shorter than a and not longer than b, for the text to resemble human speech more. Help Anfisa.

## Input

The first line contains three integers k, a and b (1 ≤ k ≤ 200, 1 ≤ a ≤ b ≤ 200). The second line contains a sequence of lowercase Latin letters — the text typed by Anfisa. It is guaranteed that the given line is not empty and its length does not exceed 200 symbols.

## Output

Print k lines, each of which contains no less than a and no more than b symbols — Anfisa's text divided into lines. It is not allowed to perform any changes in the text, such as: deleting or adding symbols, changing their order, etc. If the solution is not unique, print any of them. If there is no solution, print "No solution" (without quotes).

## Sample 1

Input

```text
3 2 5
abrakadabra
```

Output

```text
ab
rakad
abra
```

## Sample 2

Input

```text
4 1 2
abrakadabra
```

Output

```text
No solution
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
