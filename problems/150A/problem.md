# 150A · Win or Freeze

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">games</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/150/A) · Rating 1400

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

You can't possibly imagine how cold our friends are this winter in Nvodsk! Two of them play the following game to warm up: initially a piece of paper has an integer q. During a move a player should write any integer number that is a non-trivial divisor of the last written number. Then he should run this number of circles around the hotel. Let us remind you that a number's divisor is called non-trivial if it is different from one and from the divided number itself.

The first person who can't make a move wins as he continues to lie in his warm bed under three blankets while the other one keeps running. Determine which player wins considering that both players play optimally. If the first player wins, print any winning first move.

## Input

The first line contains the only integer q (1 ≤ q ≤ 1013).

Please do not use the %lld specificator to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specificator.

## Output

In the first line print the number of the winning player (1 or 2). If the first player wins then the second line should contain another integer — his first move (if the first player can't even make the first move, print 0). If there are multiple solutions, print any of them.

## Sample 1

Input

```text
6
```

Output

```text
2
```

## Sample 2

Input

```text
30
```

Output

```text
1
6
```

## Sample 3

Input

```text
1
```

Output

```text
1
0
```

## Note

Number 6 has only two non-trivial divisors: 2 and 3. It is impossible to make a move after the numbers 2 and 3 are written, so both of them are winning, thus, number 6 is the losing number. A player can make a move and write number 6 after number 30; 6, as we know, is a losing number. Thus, this move will bring us the victory.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
