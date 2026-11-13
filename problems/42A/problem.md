# 42A · Guilty — to the kitchen!

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/42/A) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

It's a very unfortunate day for Volodya today. He got bad mark in algebra and was therefore forced to do some work in the kitchen, namely to cook borscht (traditional Russian soup). This should also improve his algebra skills.

According to the borscht recipe it consists of n ingredients that have to be mixed in proportion $$(a_{1}:a_{2}:\ldots:a_{n})$$ litres (thus, there should be a1 ·x, ..., an ·x litres of corresponding ingredients mixed for some non-negative x). In the kitchen Volodya found out that he has b1, ..., bn litres of these ingredients at his disposal correspondingly. In order to correct his algebra mistakes he ought to cook as much soup as possible in a V litres volume pan (which means the amount of soup cooked can be between 0 and V litres). What is the volume of borscht Volodya will cook ultimately?

## Input

The first line of the input contains two space-separated integers n and V (1 ≤ n ≤ 20, 1 ≤ V ≤ 10000). The next line contains n space-separated integers ai (1 ≤ ai ≤ 100). Finally, the last line contains n space-separated integers bi (0 ≤ bi ≤ 100).

## Output

Your program should output just one real number — the volume of soup that Volodya will cook. Your answer must have a relative or absolute error less than 10 - 4.

## Sample 1

Input

```text
1 100
1
40
```

Output

```text
40.0
```

## Sample 2

Input

```text
2 100
1 1
25 30
```

Output

```text
50.0
```

## Sample 3

Input

```text
2 100
1 1
60 60
```

Output

```text
100.0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
