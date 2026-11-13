# 131D · Subway

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/131/D) · Rating 1600

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

A subway scheme, classic for all Berland cities is represented by a set of n stations connected by n passages, each of which connects exactly two stations and does not pass through any others. Besides, in the classic scheme one can get from any station to any other one along the passages. The passages can be used to move in both directions. Between each pair of stations there is no more than one passage.

Berland mathematicians have recently proved a theorem that states that any classic scheme has a ringroad. There can be only one ringroad. In other words, in any classic scheme one can find the only scheme consisting of stations (where any two neighbouring ones are linked by a passage) and this cycle doesn't contain any station more than once.

This invention had a powerful social impact as now the stations could be compared according to their distance from the ringroad. For example, a citizen could say "I live in three passages from the ringroad" and another one could reply "you loser, I live in one passage from the ringroad". The Internet soon got filled with applications that promised to count the distance from the station to the ringroad (send a text message to a short number...).

The Berland government decided to put an end to these disturbances and start to control the situation. You are requested to write a program that can determine the remoteness from the ringroad for each station by the city subway scheme.

## Input

The first line contains an integer n (3 ≤ n ≤ 3000), n is the number of stations (and trains at the same time) in the subway scheme. Then n lines contain descriptions of the trains, one per line. Each line contains a pair of integers xi, yi (1 ≤ xi, yi ≤ n) and represents the presence of a passage from station xi to station yi. The stations are numbered from 1 to n in an arbitrary order. It is guaranteed that xi ≠ yi and that no pair of stations contain more than one passage. The passages can be used to travel both ways. It is guaranteed that the given description represents a classic subway scheme.

## Output

Print n numbers. Separate the numbers by spaces, the i-th one should be equal to the distance of the i-th station from the ringroad. For the ringroad stations print number 0.

## Sample 1

Input

```text
4
1 3
4 3
4 2
1 2
```

Output

```text
0 0 0 0
```

## Sample 2

Input

```text
6
1 2
3 4
6 4
2 3
1 3
3 5
```

Output

```text
0 0 0 1 1 2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
