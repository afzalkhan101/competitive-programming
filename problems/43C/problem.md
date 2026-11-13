# 43C · Lucky Tickets

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/43/C) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya thinks that lucky tickets are the tickets whose numbers are divisible by 3. He gathered quite a large collection of such tickets but one day his younger brother Leonid was having a sulk and decided to destroy the collection. First he tore every ticket exactly in two, but he didn’t think it was enough and Leonid also threw part of the pieces away. Having seen this, Vasya got terrified but still tried to restore the collection. He chose several piece pairs and glued each pair together so that each pair formed a lucky ticket. The rest of the pieces Vasya threw away reluctantly. Thus, after the gluing of the 2t pieces he ended up with t tickets, each of which was lucky.

When Leonid tore the tickets in two pieces, one piece contained the first several letters of his number and the second piece contained the rest.

Vasya can glue every pair of pieces in any way he likes, but it is important that he gets a lucky ticket in the end. For example, pieces 123 and 99 can be glued in two ways: 12399 and 99123.

What maximum number of tickets could Vasya get after that?

## Input

The first line contains integer n (1 ≤ n ≤ 104) — the number of pieces. The second line contains n space-separated numbers ai (1 ≤ ai ≤ 108) — the numbers on the pieces. Vasya can only glue the pieces in pairs. Even if the number of a piece is already lucky, Vasya should glue the piece with some other one for it to count as lucky. Vasya does not have to use all the pieces. The numbers on the pieces an on the resulting tickets may coincide.

## Output

Print the single number — the maximum number of lucky tickets that will be able to be restored. Don't forget that every lucky ticket is made of exactly two pieces glued together.

## Sample 1

Input

```text
3
123 123 99
```

Output

```text
1
```

## Sample 2

Input

```text
6
1 1 1 23 10 3
```

Output

```text
1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
