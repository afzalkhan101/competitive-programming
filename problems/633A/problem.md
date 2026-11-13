# 633A · Ebony and Ivory

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/633/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Dante is engaged in a fight with "The Savior". Before he can fight it with his sword, he needs to break its shields. He has two guns, Ebony and Ivory, each of them is able to perform any non-negative number of shots.

For every bullet that hits the shield, Ebony deals a units of damage while Ivory deals b units of damage. In order to break the shield Dante has to deal exactly c units of damage. Find out if this is possible.

## Input

The first line of the input contains three integers a, b, c (1 ≤ a, b ≤ 100, 1 ≤ c ≤ 10 000) — the number of units of damage dealt by Ebony gun and Ivory gun, and the total number of damage required to break the shield, respectively.

## Output

Print "Yes" (without quotes) if Dante can deal exactly c damage to the shield and "No" (without quotes) otherwise.

## Sample 1

Input

```text
4 6 15
```

Output

```text
No
```

## Sample 2

Input

```text
3 2 7
```

Output

```text
Yes
```

## Sample 3

Input

```text
6 11 6
```

Output

```text
Yes
```

## Note

In the second sample, Dante can fire 1 bullet from Ebony and 2 from Ivory to deal exactly 1·3 + 2·2 = 7 damage. In the third sample, Dante can fire 1 bullet from ebony and no bullets from ivory to do 1·6 + 0·11 = 6 damage.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
