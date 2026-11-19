<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 245B · Internet Address

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/245/B) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya is an active Internet user. One day he came across an Internet resource he liked, so he wrote its address in the notebook. We know that the address of the written resource has format:

<protocol>://<domain>.ru[/<context>]

where:

- <protocol> can equal either "http" (without the quotes) or "ftp" (without the quotes),
- <domain> is a non-empty string, consisting of lowercase English letters,
- the /<context> part may not be present. If it is present, then <context> is a non-empty string, consisting of lowercase English letters.

If string <context> isn't present in the address, then the additional character "/" isn't written. Thus, the address has either two characters "/" (the ones that go before the domain), or three (an extra one in front of the context).

When the boy came home, he found out that the address he wrote in his notebook had no punctuation marks. Vasya must have been in a lot of hurry and didn't write characters ":", "/", ".".

Help Vasya to restore the possible address of the recorded Internet resource.

## Input

The first line contains a non-empty string that Vasya wrote out in his notebook. This line consists of lowercase English letters only.

It is guaranteed that the given string contains at most 50 letters. It is guaranteed that the given string can be obtained from some correct Internet resource address, described above.

## Output

Print a single line — the address of the Internet resource that Vasya liked. If there are several addresses that meet the problem limitations, you are allowed to print any of them.

## Sample 1

Input

```text
httpsunrux
```

Output

```text
http://sun.ru/x
```

## Sample 2

Input

```text
ftphttprururu
```

Output

```text
ftp://http.ru/ruru
```

## Note

In the second sample there are two more possible answers: "ftp://httpruru.ru" and "ftp://httpru.ru/ru".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
