<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 6C · Alice, Bob and Chocolate

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">two pointers</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/6/C) · Rating 1200

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

Alice and Bob like games. And now they are ready to start a new game. They have placed n chocolate bars in a line. Alice starts to eat chocolate bars one by one from left to right, and Bob — from right to left. For each chocololate bar the time, needed for the player to consume it, is known (Alice and Bob eat them with equal speed). When the player consumes a chocolate bar, he immediately starts with another. It is not allowed to eat two chocolate bars at the same time, to leave the bar unfinished and to make pauses. If both players start to eat the same bar simultaneously, Bob leaves it to Alice as a true gentleman.

How many bars each of the players will consume?

## Input

The first line contains one integer n (1 ≤ n ≤ 105) — the amount of bars on the table. The second line contains a sequence t1, t2, ..., tn (1 ≤ ti ≤ 1000), where ti is the time (in seconds) needed to consume the i-th bar (in the order from left to right).

## Output

Print two numbers a and b, where a is the amount of bars consumed by Alice, and b is the amount of bars consumed by Bob.

## Sample 1

Input

```text
5
2 9 8 2 7
```

Output

```text
2 3
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
