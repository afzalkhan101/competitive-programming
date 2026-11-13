# 519C · A and B and Team Training

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/519/C) · Rating 1300

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

A and B are preparing themselves for programming contests.

An important part of preparing for a competition is sharing programming knowledge from the experienced members to those who are just beginning to deal with the contests. Therefore, during the next team training A decided to make teams so that newbies are solving problems together with experienced participants.

A believes that the optimal team of three people should consist of one experienced participant and two newbies. Thus, each experienced participant can share the experience with a large number of people.

However, B believes that the optimal team should have two experienced members plus one newbie. Thus, each newbie can gain more knowledge and experience.

As a result, A and B have decided that all the teams during the training session should belong to one of the two types described above. Furthermore, they agree that the total number of teams should be as much as possible.

There are n experienced members and m newbies on the training session. Can you calculate what maximum number of teams can be formed?

## Input

The first line contains two integers n and m (0 ≤ n, m ≤ 5·105) — the number of experienced participants and newbies that are present at the training session.

## Output

Print the maximum number of teams that can be formed.

## Sample 1

Input

```text
2 6
```

Output

```text
2
```

## Sample 2

Input

```text
4 5
```

Output

```text
3
```

## Note

Let's represent the experienced players as XP and newbies as NB.

In the first test the teams look as follows: (XP, NB, NB), (XP, NB, NB).

In the second test sample the teams look as follows: (XP, NB, NB), (XP, NB, NB), (XP, XP, NB).

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
