<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 16B · Burglar and Matches

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/16/B) · Rating 900

Time: 0.5 seconds · Memory: 64.0 MB

## Problem

A burglar got into a matches warehouse and wants to steal as many matches as possible. In the warehouse there are m containers, in the i-th container there are ai matchboxes, and each matchbox contains bi matches. All the matchboxes are of the same size. The burglar's rucksack can hold n matchboxes exactly. Your task is to find out the maximum amount of matches that a burglar can carry away. He has no time to rearrange matches in the matchboxes, that's why he just chooses not more than n matchboxes so that the total amount of matches in them is maximal.

## Input

The first line of the input contains integer n (1 ≤ n ≤ 2·108) and integer m (1 ≤ m ≤ 20). The i + 1-th line contains a pair of numbers ai and bi (1 ≤ ai ≤ 108, 1 ≤ bi ≤ 10). All the input numbers are integer.

## Output

Output the only number — answer to the problem.

## Sample 1

Input

```text
7 3
5 10
2 5
3 6
```

Output

```text
62
```

## Sample 2

Input

```text
3 3
1 3
2 2
3 1
```

Output

```text
7
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
