# 39B · Company Income Growth

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/39/B) · Rating 1300

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

Petya works as a PR manager for a successful Berland company BerSoft. He needs to prepare a presentation on the company income growth since 2001 (the year of its founding) till now. Petya knows that in 2001 the company income amounted to a1 billion bourles, in 2002 — to a2 billion, ..., and in the current (2000 + n)-th year — an billion bourles. On the base of the information Petya decided to show in his presentation the linear progress history which is in his opinion perfect. According to a graph Petya has already made, in the first year BerSoft company income must amount to 1 billion bourles, in the second year — 2 billion bourles etc., each following year the income increases by 1 billion bourles. Unfortunately, the real numbers are different from the perfect ones. Among the numbers ai can even occur negative ones that are a sign of the company’s losses in some years. That is why Petya wants to ignore some data, in other words, cross some numbers ai from the sequence and leave only some subsequence that has perfect growth.

Thus Petya has to choose a sequence of years y1, y2, ..., yk,so that in the year y1 the company income amounted to 1 billion bourles, in the year y2 — 2 billion bourles etc., in accordance with the perfect growth dynamics. Help him to choose the longest such sequence.

## Input

The first line contains an integer n (1 ≤ n ≤ 100). The next line contains n integers ai ( - 100 ≤ ai ≤ 100). The number ai determines the income of BerSoft company in the (2000 + i)-th year. The numbers in the line are separated by spaces.

## Output

Output k — the maximum possible length of a perfect sequence. In the next line output the sequence of years y1, y2, ..., yk. Separate the numbers by spaces. If the answer is not unique, output any. If no solution exist, output one number 0.

## Sample 1

Input

```text
10
-2 1 1 3 2 3 4 -10 -2 5
```

Output

```text
5
2002 2005 2006 2007 2010
```

## Sample 2

Input

```text
3
-1 -2 -3
```

Output

```text
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
