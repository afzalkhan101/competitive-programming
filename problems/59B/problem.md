# 59B · Fortune Telling

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">implementation</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/59/B) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Marina loves Sasha. But she keeps wondering whether Sasha loves her. Of course, the best way to know it is fortune telling. There are many ways of telling fortune, but Marina has picked the easiest one. She takes in her hand one or several camomiles and tears off the petals one by one. After each petal she pronounces alternatively "Loves" and "Doesn't love", at that Marina always starts with "Loves". There are n camomiles growing in the field, possessing the numbers of petals equal to a1, a2, ... an. Marina wants to pick a bouquet with the maximal possible total number of petals so that the result would still be "Loves". Help her do that; find the maximal number of petals possible in the bouquet.

## Input

The first line contains an integer n (1 ≤ n ≤ 100), which is the number of flowers growing in the field. The second line contains n integers ai (1 ≤ ai ≤ 100) which represent the number of petals on a given i-th camomile.

## Output

Print a single number which is the maximal number of petals in the bouquet, the fortune telling on which would result in "Loves". If there are no such bouquet, print 0 instead. The bouquet may consist of a single flower.

## Sample 1

Input

```text
1
1
```

Output

```text
1
```

## Sample 2

Input

```text
1
2
```

Output

```text
0
```

## Sample 3

Input

```text
3
5 6 7
```

Output

```text
13
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
