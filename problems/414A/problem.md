<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 414A · Mashmokh and Numbers

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/414/A) · Rating 1500

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

It's holiday. Mashmokh and his boss, Bimokh, are playing a game invented by Mashmokh.

In this game Mashmokh writes sequence of n distinct integers on the board. Then Bimokh makes several (possibly zero) moves. On the first move he removes the first and the second integer from from the board, on the second move he removes the first and the second integer of the remaining sequence from the board, and so on. Bimokh stops when the board contains less than two numbers. When Bimokh removes numbers x and y from the board, he gets gcd(x, y) points. At the beginning of the game Bimokh has zero points.

Mashmokh wants to win in the game. For this reason he wants his boss to get exactly k points in total. But the guy doesn't know how choose the initial sequence in the right way.

Please, help him. Find n distinct integers a1, a2, ..., an such that his boss will score exactly k points. Also Mashmokh can't memorize too huge numbers. Therefore each of these integers must be at most 109.

## Input

The first line of input contains two space-separated integers n, k (1 ≤ n ≤ 105; 0 ≤ k ≤ 108).

## Output

If such sequence doesn't exist output -1 otherwise output n distinct space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109).

## Sample 1

Input

```text
5 2
```

Output

```text
1 2 3 4 5
```

## Sample 2

Input

```text
5 3
```

Output

```text
2 4 3 7 1
```

## Sample 3

Input

```text
7 2
```

Output

```text
-1
```

## Note

gcd(x, y) is greatest common divisor of x and y.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
