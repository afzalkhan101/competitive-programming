<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 164A · Variable, or There and Back Again

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/164/A) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Life is not easy for the perfectly common variable named Vasya. Wherever it goes, it is either assigned a value, or simply ignored, or is being used!

Vasya's life goes in states of a program. In each state, Vasya can either be used (for example, to calculate the value of another variable), or be assigned a value, or ignored. Between some states are directed (oriented) transitions.

A path is a sequence of states v1, v2, ..., vx, where for any 1 ≤ i < x exists a transition from vi to vi + 1.

Vasya's value in state v is interesting to the world, if exists path p1, p2, ..., pk such, that pi = v for some i (1 ≤ i ≤ k), in state p1 Vasya gets assigned a value, in state pk Vasya is used and there is no state pi (except for p1) where Vasya gets assigned a value.

Help Vasya, find the states in which Vasya's value is interesting to the world.

## Input

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 105) — the numbers of states and transitions, correspondingly.

The second line contains space-separated n integers f1, f2, ..., fn (0 ≤ fi ≤ 2), fi described actions performed upon Vasya in state i: 0 represents ignoring, 1 — assigning a value, 2 — using.

Next m lines contain space-separated pairs of integers ai, bi (1 ≤ ai, bi ≤ n, ai ≠ bi), each pair represents the transition from the state number ai to the state number bi. Between two states can be any number of transitions.

## Output

Print n integers r1, r2, ..., rn, separated by spaces or new lines. Number ri should equal 1, if Vasya's value in state i is interesting to the world and otherwise, it should equal 0. The states are numbered from 1 to n in the order, in which they are described in the input.

## Sample 1

Input

```text
4 3
1 0 0 2
1 2
2 3
3 4
```

Output

```text
1
1
1
1
```

## Sample 2

Input

```text
3 1
1 0 2
1 3
```

Output

```text
1
0
1
```

## Sample 3

Input

```text
3 1
2 0 1
1 3
```

Output

```text
0
0
0
```

## Note

In the first sample the program states can be used to make the only path in which the value of Vasya interests the world, 1 $$\rightarrow$$ 2 $$\rightarrow$$ 3 $$\rightarrow$$ 4; it includes all the states, so in all of them Vasya's value is interesting to the world.

The second sample the only path in which Vasya's value is interesting to the world is , — 1 $$\rightarrow$$ 3; state 2 is not included there.

In the third sample we cannot make from the states any path in which the value of Vasya would be interesting to the world, so the value of Vasya is never interesting to the world.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
