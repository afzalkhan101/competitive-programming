# 745A · Hongcow Learns the Cyclic Shift

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/745/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Hongcow is learning to spell! One day, his teacher gives him a word that he needs to learn to spell. Being a dutiful student, he immediately learns how to spell the word.

Hongcow has decided to try to make new words from this one. He starts by taking the word he just learned how to spell, and moves the last character of the word to the beginning of the word. He calls this a cyclic shift. He can apply cyclic shift many times. For example, consecutively applying cyclic shift operation to the word "abracadabra" Hongcow will get words "aabracadabr", "raabracadab" and so on.

Hongcow is now wondering how many distinct words he can generate by doing the cyclic shift arbitrarily many times. The initial string is also counted.

## Input

The first line of input will be a single string s (1 ≤ |s| ≤ 50), the word Hongcow initially learns how to spell. The string s consists only of lowercase English letters ('a'–'z').

## Output

Output a single integer equal to the number of distinct strings that Hongcow can obtain by applying the cyclic shift arbitrarily many times to the given string.

## Sample 1

Input

```text
abcd
```

Output

```text
4
```

## Sample 2

Input

```text
bbb
```

Output

```text
1
```

## Sample 3

Input

```text
yzyz
```

Output

```text
2
```

## Note

For the first sample, the strings Hongcow can generate are "abcd", "dabc", "cdab", and "bcda".

For the second sample, no matter how many times Hongcow does the cyclic shift, Hongcow can only generate "bbb".

For the third sample, the two strings Hongcow can generate are "yzyz" and "zyzy".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
