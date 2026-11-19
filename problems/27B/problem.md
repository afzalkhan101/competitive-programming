<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 27B · Tournament

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">bitmasks</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/27/B) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The tournament «Sleepyhead-2010» in the rapid falling asleep has just finished in Berland. n best participants from the country have participated in it. The tournament consists of games, each of them is a match between two participants. n·(n - 1) / 2 games were played during the tournament, and each participant had a match with each other participant.

The rules of the game are quite simple — the participant who falls asleep first wins. The secretary made a record of each game in the form «xi yi», where xi and yi are the numbers of participants. The first number in each pair is a winner (i.e. xi is a winner and yi is a loser). There is no draws.

Recently researches form the «Institute Of Sleep» have found that every person is characterized by a value pj — the speed of falling asleep. The person who has lower speed wins. Every person has its own value pj, constant during the life.

It is known that all participants of the tournament have distinct speeds of falling asleep. Also it was found that the secretary made records about all the games except one. You are to find the result of the missing game.

## Input

The first line contains one integer n (3 ≤ n ≤ 50) — the number of participants. The following n·(n - 1) / 2 - 1 lines contain the results of the games. Each game is described in a single line by two integers xi, yi (1 ≤ xi, yi ≤ n, xi ≠ yi), where xi и yi are the numbers of the opponents in this game. It is known that during the tournament each of the n participants played n - 1 games, one game with each other participant.

## Output

Output two integers x and y — the missing record. If there are several solutions, output any of them.

## Sample 1

Input

```text
4
4 2
4 1
2 3
2 1
3 1
```

Output

```text
4 3
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
