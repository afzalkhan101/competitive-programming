# 757B · Bash's Big Day

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">greedy</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/757/B) · Rating 1400

Time: 2.0 seconds · Memory: 512.0 MB

## Problem

Bash has set out on a journey to become the greatest Pokemon master. To get his first Pokemon, he went to Professor Zulu's Lab. Since Bash is Professor Zulu's favourite student, Zulu allows him to take as many Pokemon from his lab as he pleases.

But Zulu warns him that a group of k > 1 Pokemon with strengths {s1, s2, s3, ..., sk} tend to fight among each other if gcd(s1, s2, s3, ..., sk) = 1 (see notes for gcd definition).

Bash, being smart, does not want his Pokemon to fight among each other. However, he also wants to maximize the number of Pokemon he takes from the lab. Can you help Bash find out the maximum number of Pokemon he can take?

Note: A Pokemon cannot fight with itself.

## Input

The input consists of two lines.

The first line contains an integer n (1 ≤ n ≤ 105), the number of Pokemon in the lab.

The next line contains n space separated integers, where the i-th of them denotes si (1 ≤ si ≤ 105), the strength of the i-th Pokemon.

## Output

Print single integer — the maximum number of Pokemons Bash can take.

## Sample 1

Input

```text
3
2 3 4
```

Output

```text
2
```

## Sample 2

Input

```text
5
2 3 4 6 7
```

Output

```text
3
```

## Note

gcd (greatest common divisor) of positive integers set {a1, a2, ..., an} is the maximum positive integer that divides all the integers {a1, a2, ..., an}.

In the first sample, we can take Pokemons with strengths {2, 4} since gcd(2, 4) = 2.

In the second sample, we can take Pokemons with strengths {2, 4, 6}, and there is no larger group with gcd ≠ 1.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
