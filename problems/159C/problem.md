# 159C · String Manipulation 1.0

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">*special</span><span class="practice-tag">binary search</span><span class="practice-tag">brute force</span><span class="practice-tag">data structures</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/159/C) · Rating 1400

Time: 3.0 seconds · Memory: 256.0 MB

## Problem

One popular website developed an unusual username editing procedure. One can change the username only by deleting some characters from it: to change the current name s, a user can pick number p and character c and delete the p-th occurrence of character c from the name. After the user changed his name, he can't undo the change.

For example, one can change name "arca" by removing the second occurrence of character "a" to get "arc".

Polycarpus learned that some user initially registered under nickname t, where t is a concatenation of k copies of string s. Also, Polycarpus knows the sequence of this user's name changes. Help Polycarpus figure out the user's final name.

## Input

The first line contains an integer k (1 ≤ k ≤ 2000). The second line contains a non-empty string s, consisting of lowercase Latin letters, at most 100 characters long. The third line contains an integer n (0 ≤ n ≤ 20000) — the number of username changes. Each of the next n lines contains the actual changes, one per line. The changes are written as "pi ci" (without the quotes), where pi (1 ≤ pi ≤ 200000) is the number of occurrences of letter ci, ci is a lowercase Latin letter. It is guaranteed that the operations are correct, that is, the letter to be deleted always exists, and after all operations not all letters are deleted from the name. The letters' occurrences are numbered starting from 1.

## Output

Print a single string — the user's final name after all changes are applied to it.

## Sample 1

Input

```text
2
bac
3
2 a
1 b
2 c
```

Output

```text
acb
```

## Sample 2

Input

```text
1
abacaba
4
1 a
1 a
1 c
2 b
```

Output

```text
baa
```

## Note

Let's consider the first sample. Initially we have name "bacbac"; the first operation transforms it into "bacbc", the second one — to "acbc", and finally, the third one transforms it into "acb".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
