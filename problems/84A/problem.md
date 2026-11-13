# 84A · Toy Army

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/84/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The hero of our story, Valera, and his best friend Arcady are still in school, and therefore they spend all the free time playing turn-based strategy "GAGA: Go And Go Again". The gameplay is as follows.

There are two armies on the playing field each of which consists of n men (n is always even). The current player specifies for each of her soldiers an enemy's soldier he will shoot (a target) and then all the player's soldiers shot simultaneously. This is a game world, and so each soldier shoots perfectly, that is he absolutely always hits the specified target. If an enemy soldier is hit, he will surely die. It may happen that several soldiers had been indicated the same target. Killed soldiers do not participate in the game anymore.

The game "GAGA" consists of three steps: first Valera makes a move, then Arcady, then Valera again and the game ends.

You are asked to calculate the maximum total number of soldiers that may be killed during the game.

## Input

The input data consist of a single integer n (2 ≤ n ≤ 108, n is even). Please note that before the game starts there are 2n soldiers on the fields.

## Output

Print a single number — a maximum total number of soldiers that could be killed in the course of the game in three turns.

## Sample 1

Input

```text
2
```

Output

```text
3
```

## Sample 2

Input

```text
4
```

Output

```text
6
```

## Note

The first sample test:

1) Valera's soldiers 1 and 2 shoot at Arcady's soldier 1.

2) Arcady's soldier 2 shoots at Valera's soldier 1.

3) Valera's soldier 1 shoots at Arcady's soldier 2.

There are 3 soldiers killed in total: Valera's soldier 1 and Arcady's soldiers 1 and 2.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
