# 114B · PFAST Inc.

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">bitmasks</span><span class="practice-tag">brute force</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/114/B) · Rating 1500

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

When little Petya grew up and entered the university, he started to take part in АСМ contests. Later he realized that he doesn't like how the АСМ contests are organised: the team could only have three members (and he couldn't take all his friends to the competitions and distribute the tasks between the team members efficiently), so he decided to organize his own contests PFAST Inc. — Petr and Friends Are Solving Tasks Corporation. PFAST Inc. rules allow a team to have unlimited number of members.

To make this format of contests popular he organised his own tournament. To create the team he will prepare for the contest organised by the PFAST Inc. rules, he chose several volunteers (up to 16 people) and decided to compile a team from them. Petya understands perfectly that if a team has two people that don't get on well, then the team will perform poorly. Put together a team with as many players as possible given that all players should get on well with each other.

## Input

The first line contains two integer numbers n (1 ≤ n ≤ 16) — the number of volunteers, and m ($$0 \leq m \leq \frac{n(n-1)}{2}$$) — the number of pairs that do not get on. Next n lines contain the volunteers' names (each name is a non-empty string consisting of no more than 10 uppercase and/or lowercase Latin letters). Next m lines contain two names — the names of the volunteers who do not get on. The names in pair are separated with a single space. Each pair of volunteers who do not get on occurs exactly once. The strings are case-sensitive. All n names are distinct.

## Output

The first output line should contain the single number k — the number of people in the sought team. Next k lines should contain the names of the sought team's participants in the lexicographical order. If there are several variants to solve the problem, print any of them. Petya might not be a member of the sought team.

## Sample 1

Input

```text
3 1
Petya
Vasya
Masha
Petya Vasya
```

Output

```text
2
Masha
Petya
```

## Sample 2

Input

```text
3 0
Pasha
Lesha
Vanya
```

Output

```text
3
Lesha
Pasha
Vanya
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
