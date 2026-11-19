<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 31B · Sysadmin Bob

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/31/B) · Rating 1500

Time: 0.5 seconds · Memory: 256.0 MB

## Problem

Email address in Berland is a string of the form A@B, where A and B are arbitrary strings consisting of small Latin letters.

Bob is a system administrator in «Bersoft» company. He keeps a list of email addresses of the company's staff. This list is as a large string, where all addresses are written in arbitrary order, separated by commas. The same address can be written more than once.

Suddenly, because of unknown reasons, all commas in Bob's list disappeared. Now Bob has a string, where all addresses are written one after another without any separators, and there is impossible to determine, where the boundaries between addresses are. Unfortunately, on the same day his chief asked him to bring the initial list of addresses. Now Bob wants to disjoin addresses in some valid way. Help him to do that.

## Input

The first line contains the list of addresses without separators. The length of this string is between 1 and 200, inclusive. The string consists only from small Latin letters and characters «@».

## Output

If there is no list of the valid (according to the Berland rules) email addresses such that after removing all commas it coincides with the given string, output No solution. In the other case, output the list. The same address can be written in this list more than once. If there are several solutions, output any of them.

## Sample 1

Input

```text
a@aa@a
```

Output

```text
a@a,a@a
```

## Sample 2

Input

```text
a@a@a
```

Output

```text
No solution
```

## Sample 3

Input

```text
@aa@a
```

Output

```text
No solution
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
