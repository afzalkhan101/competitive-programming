<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 106A · Card Game

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/106/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

There is a card game called "Durak", which means "Fool" in Russian. The game is quite popular in the countries that used to form USSR. The problem does not state all the game's rules explicitly — you can find them later yourselves if you want.

To play durak you need a pack of 36 cards. Each card has a suit ("S", "H", "D" and "C") and a rank (in the increasing order "6", "7", "8", "9", "T", "J", "Q", "K" and "A"). At the beginning of the game one suit is arbitrarily chosen as trump.

The players move like that: one player puts one or several of his cards on the table and the other one should beat each of them with his cards.

A card beats another one if both cards have similar suits and the first card has a higher rank then the second one. Besides, a trump card can beat any non-trump card whatever the cards’ ranks are. In all other cases you can not beat the second card with the first one.

You are given the trump suit and two different cards. Determine whether the first one beats the second one or not.

## Input

The first line contains the tramp suit. It is "S", "H", "D" or "C".

The second line contains the description of the two different cards. Each card is described by one word consisting of two symbols. The first symbol stands for the rank ("6", "7", "8", "9", "T", "J", "Q", "K" and "A"), and the second one stands for the suit ("S", "H", "D" and "C").

## Output

Print "YES" (without the quotes) if the first cards beats the second one. Otherwise, print "NO" (also without the quotes).

## Sample 1

Input

```text
H
QH 9S
```

Output

```text
YES
```

## Sample 2

Input

```text
S
8D 6D
```

Output

```text
YES
```

## Sample 3

Input

```text
C
7H AS
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
