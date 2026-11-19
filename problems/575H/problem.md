<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 575H · Bots

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">combinatorics</span><span class="practice-tag">dp</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/575/H) · Rating 1800

Time: 1.5 seconds · Memory: 256.0 MB

## Problem

Sasha and Ira are two best friends. But they aren’t just friends, they are software engineers and experts in artificial intelligence. They are developing an algorithm for two bots playing a two-player game. The game is cooperative and turn based. In each turn, one of the players makes a move (it doesn’t matter which player, it's possible that players turns do not alternate).

Algorithm for bots that Sasha and Ira are developing works by keeping track of the state the game is in. Each time either bot makes a move, the state changes. And, since the game is very dynamic, it will never go back to the state it was already in at any point in the past.

Sasha and Ira are perfectionists and want their algorithm to have an optimal winning strategy. They have noticed that in the optimal winning strategy, both bots make exactly N moves each. But, in order to find the optimal strategy, their algorithm needs to analyze all possible states of the game (they haven’t learned about alpha-beta pruning yet) and pick the best sequence of moves.

They are worried about the efficiency of their algorithm and are wondering what is the total number of states of the game that need to be analyzed?

## Input

The first and only line contains integer N.

- 1 ≤ N ≤ 106

## Output

Output should contain a single integer – number of possible states modulo 109 + 7.

## Sample 1

Input

```text
2
```

Output

```text
19
```

## Note

Start: Game is in state A.

- Turn 1: Either bot can make a move (first bot is red and second bot is blue), so there are two possible states after the first turn – B and C.
- Turn 2: In both states B and C, either bot can again make a turn, so the list of possible states is expanded to include D, E, F and G.
- Turn 3: Red bot already did N=2 moves when in state D, so it cannot make any more moves there. It can make moves when in state E, F and G, so states I, K and M are added to the list. Similarly, blue bot cannot make a move when in state G, but can when in D, E and F, so states H, J and L are added.
- Turn 4: Red bot already did N=2 moves when in states H, I and K, so it can only make moves when in J, L and M, so states P, R and S are added. Blue bot cannot make a move when in states J, L and M, but only when in H, I and K, so states N, O and Q are added.

Overall, there are 19 possible states of the game their algorithm needs to analyze.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
