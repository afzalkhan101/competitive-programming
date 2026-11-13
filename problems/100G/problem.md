# 100G · Name the album

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">*special</span><span class="practice-tag">data structures</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/100/G) · Rating 1800

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

The famous singer, Aryo, is going to publish a new album of his great work!

Unfortunately these days, there are many albums, Aryo wants to choose a new name for his album, a name that has not been used or at least has not been used recently.

He has a list of all used album names together with the year the albums were published. He also has a list of suitable names for his album.

If he finds a suitable name which has not been used before, he'll use it. Otherwise he will use the name which was used as long ago as possible. If two such names are found (that haven't been used or were used at the same year), he uses the name that is alphabetically latest.

Help him name his album.

## Input

The first line contains a single integer n (0 ≤ n ≤ 105), the number of used names.

The following n lines each contain a string (the album name) and an integer (the year album was published). Album names are made of lowercase Latin letters and contain at most 14 letters. The year is in range [1900, 2011].

The following line contains a single integer m (1 ≤ m ≤ 104), the number of suitable album names.

The following m lines each contain a string — a suitable name. It contains at most 14 lowercase Latin letters.

All album names and suitable names are non-empty.

## Output

Write a single string. The name of the new album.

## Sample 1

Input

```text
3
eyesonme 2008
anewdayhascome 2002
oneheart 2003
2
oneheart
bienbien
```

Output

```text
bienbien
```

## Sample 2

Input

```text
2
nasimevasl 2003
basetareha 2006
2
nasimevasl
basetareha
```

Output

```text
nasimevasl
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
