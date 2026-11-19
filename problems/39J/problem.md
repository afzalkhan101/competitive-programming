<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 39J · Spelling Check

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">hashing</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/39/J) · Rating 1500

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Petya has noticed that when he types using a keyboard, he often presses extra buttons and adds extra letters to the words. Of course, the spell-checking system underlines the words for him and he has to click every word and choose the right variant. Petya got fed up with correcting his mistakes himself, that’s why he decided to invent the function that will correct the words itself. Petya started from analyzing the case that happens to him most of the time, when all one needs is to delete one letter for the word to match a word from the dictionary. Thus, Petya faces one mini-task: he has a printed word and a word from the dictionary, and he should delete one letter from the first word to get the second one. And now the very non-trivial question that Petya faces is: which letter should he delete?

## Input

The input data contains two strings, consisting of lower-case Latin letters. The length of each string is from 1 to 106 symbols inclusive, the first string contains exactly 1 symbol more than the second one.

## Output

In the first line output the number of positions of the symbols in the first string, after the deleting of which the first string becomes identical to the second one. In the second line output space-separated positions of these symbols in increasing order. The positions are numbered starting from 1. If it is impossible to make the first string identical to the second string by deleting one symbol, output one number 0.

## Sample 1

Input

```text
abdrakadabra
abrakadabra
```

Output

```text
1
3
```

## Sample 2

Input

```text
aa
a
```

Output

```text
2
1 2
```

## Sample 3

Input

```text
competition
codeforces
```

Output

```text
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
