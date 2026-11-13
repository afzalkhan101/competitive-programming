# 126B · Password

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">binary search</span><span class="practice-tag">dp</span><span class="practice-tag">hashing</span><span class="practice-tag">string suffix structures</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/126/B) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Asterix, Obelix and their temporary buddies Suffix and Prefix has finally found the Harmony temple. However, its doors were firmly locked and even Obelix had no luck opening them.

A little later they found a string s, carved on a rock below the temple's gates. Asterix supposed that that's the password that opens the temple and read the string aloud. However, nothing happened. Then Asterix supposed that a password is some substring t of the string s.

Prefix supposed that the substring t is the beginning of the string s; Suffix supposed that the substring t should be the end of the string s; and Obelix supposed that t should be located somewhere inside the string s, that is, t is neither its beginning, nor its end.

Asterix chose the substring t so as to please all his companions. Besides, from all acceptable variants Asterix chose the longest one (as Asterix loves long strings). When Asterix read the substring t aloud, the temple doors opened.

You know the string s. Find the substring t or determine that such substring does not exist and all that's been written above is just a nice legend.

## Input

You are given the string s whose length can vary from 1 to 106 (inclusive), consisting of small Latin letters.

## Output

Print the string t. If a suitable t string does not exist, then print "Just a legend" without the quotes.

## Sample 1

Input

```text
fixprefixsuffix
```

Output

```text
fix
```

## Sample 2

Input

```text
abcdabc
```

Output

```text
Just a legend
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
