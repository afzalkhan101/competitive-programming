# 546D · Soldier and Number Game

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">dp</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/546/D) · Rating 1700

Time: 3.0 seconds · Memory: 256.0 MB

## Problem

Two soldiers are playing a game. At the beginning first of them chooses a positive integer n and gives it to the second soldier. Then the second one tries to make maximum possible number of rounds. Each round consists of choosing a positive integer x > 1, such that n is divisible by x and replacing n with n / x. When n becomes equal to 1 and there is no more possible valid moves the game is over and the score of the second soldier is equal to the number of rounds he performed.

To make the game more interesting, first soldier chooses n of form a! / b! for some positive integer a and b (a ≥ b). Here by k! we denote the factorial of k that is defined as a product of all positive integers not large than k.

What is the maximum possible score of the second soldier?

## Input

First line of input consists of single integer t (1 ≤ t ≤ 1 000 000) denoting number of games soldiers play.

Then follow t lines, each contains pair of integers a and b (1 ≤ b ≤ a ≤ 5 000 000) defining the value of n for a game.

## Output

For each game output a maximum score that the second soldier can get.

## Sample 1

Input

```text
2
3 1
6 3
```

Output

```text
2
5
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
