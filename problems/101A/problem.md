<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 101A · Homework

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/101/A) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Once when Gerald studied in the first year at school, his teacher gave the class the following homework. She offered the students a string consisting of n small Latin letters; the task was to learn the way the letters that the string contains are written. However, as Gerald is too lazy, he has no desire whatsoever to learn those letters. That's why he decided to lose some part of the string (not necessarily a connected part). The lost part can consist of any number of segments of any length, at any distance from each other. However, Gerald knows that if he loses more than k characters, it will be very suspicious.

Find the least number of distinct characters that can remain in the string after no more than k characters are deleted. You also have to find any possible way to delete the characters.

## Input

The first input data line contains a string whose length is equal to n (1 ≤ n ≤ 105). The string consists of lowercase Latin letters. The second line contains the number k (0 ≤ k ≤ 105).

## Output

Print on the first line the only number m — the least possible number of different characters that could remain in the given string after it loses no more than k characters.

Print on the second line the string that Gerald can get after some characters are lost. The string should have exactly m distinct characters. The final string should be the subsequence of the initial string. If Gerald can get several different strings with exactly m distinct characters, print any of them.

## Sample 1

Input

```text
aaaaa
4
```

Output

```text
1
aaaaa
```

## Sample 2

Input

```text
abacaba
4
```

Output

```text
1
aaaa
```

## Sample 3

Input

```text
abcdefgh
10
```

Output

```text
0
```

## Note

In the first sample the string consists of five identical letters but you are only allowed to delete 4 of them so that there was at least one letter left. Thus, the right answer is 1 and any string consisting of characters "a" from 1 to 5 in length.

In the second sample you are allowed to delete 4 characters. You cannot delete all the characters, because the string has length equal to 7. However, you can delete all characters apart from "a" (as they are no more than four), which will result in the "aaaa" string.

In the third sample you are given a line whose length is equal to 8, and k = 10, so that the whole line can be deleted. The correct answer is 0 and an empty string.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
