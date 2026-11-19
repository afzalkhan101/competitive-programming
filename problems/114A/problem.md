<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 114A · Cifera

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/114/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

When Petya went to school, he got interested in large numbers and what they were called in ancient times. For instance, he learned that the Russian word "tma" (which now means "too much to be counted") used to stand for a thousand and "tma tmyschaya" (which literally means "the tma of tmas") used to stand for a million.

Petya wanted to modernize the words we use for numbers and invented a word petricium that represents number k. Moreover, petricium la petricium stands for number k2, petricium la petricium la petricium stands for k3 and so on. All numbers of this form are called petriciumus cifera, and the number's importance is the number of articles la in its title.

Petya's invention brought on a challenge that needed to be solved quickly: does some number l belong to the set petriciumus cifera? As Petya is a very busy schoolboy he needs to automate the process, he asked you to solve it.

## Input

The first input line contains integer number k, the second line contains integer number l (2 ≤ k, l ≤ 231 - 1).

## Output

You should print in the first line of the output "YES", if the number belongs to the set petriciumus cifera and otherwise print "NO". If the number belongs to the set, then print on the seconds line the only number — the importance of number l.

## Sample 1

Input

```text
5
25
```

Output

```text
YES
1
```

## Sample 2

Input

```text
3
8
```

Output

```text
NO
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
