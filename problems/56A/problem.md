<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 56A · Bar

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/56/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

According to Berland laws it is only allowed to sell alcohol to people not younger than 18 years. Vasya's job is to monitor the law's enforcement. Tonight he entered a bar and saw n people sitting there. For every one of them Vasya happened to determine either the age or the drink the person is having. Vasya can check any person, i.e. learn his age and the drink he is having at the same time. What minimal number of people should Vasya check additionally to make sure that there are no clients under 18 having alcohol drinks?

The list of all alcohol drinks in Berland is: ABSINTH, BEER, BRANDY, CHAMPAGNE, GIN, RUM, SAKE, TEQUILA, VODKA, WHISKEY, WINE

## Input

The first line contains an integer n (1 ≤ n ≤ 100) which is the number of the bar's clients. Then follow n lines, each describing one visitor. A line either contains his age (an integer from 0 to 1000) or his drink (a string of capital Latin letters from 1 to 100 in length). It is guaranteed that the input data does not contain spaces and other unnecessary separators.

Only the drinks from the list given above should be considered alcohol.

## Output

Print a single number which is the number of people Vasya should check to guarantee the law enforcement.

## Sample 1

Input

```text
5
18
VODKA
COKE
19
17
```

Output

```text
2
```

## Note

In the sample test the second and fifth clients should be checked.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
