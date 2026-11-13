# 129A · Cookies

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/129/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Olga came to visit the twins Anna and Maria and saw that they have many cookies. The cookies are distributed into bags. As there are many cookies, Olga decided that it's no big deal if she steals a bag. However, she doesn't want the sisters to quarrel because of nothing when they divide the cookies. That's why Olga wants to steal a bag with cookies so that the number of cookies in the remaining bags was even, that is, so that Anna and Maria could evenly divide it into two (even 0 remaining cookies will do, just as any other even number). How many ways there are to steal exactly one cookie bag so that the total number of cookies in the remaining bags was even?

## Input

The first line contains the only integer n (1 ≤ n ≤ 100) — the number of cookie bags Anna and Maria have. The second line contains n integers ai (1 ≤ ai ≤ 100) — the number of cookies in the i-th bag.

## Output

Print in the only line the only number — the sought number of ways. If there are no such ways print 0.

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
10
1 2 2 3 4 4 4 2 2 2
```

Output

```text
8
```

## Sample 3

Input

```text
11
2 2 2 2 2 2 2 2 2 2 99
```

Output

```text
1
```

## Note

In the first sample Olga should take the only bag so that the twins ended up with the even number of cookies.

In the second sample Olga can take any of five bags with two cookies or any of three bags with four cookies — 5 + 3 = 8 ways in total.

In the third sample, no matter which bag with two cookies Olga chooses, the twins are left with 2 * 9 + 99 = 117 cookies. Thus, Olga has only one option: to take the bag with 99 cookies.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
