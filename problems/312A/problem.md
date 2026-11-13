# 312A · Whose sentence is it?

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">implementation</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/312/A) · Rating 1100

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

One day, liouzhou_101 got a chat record of Freda and Rainbow. Out of curiosity, he wanted to know which sentences were said by Freda, and which were said by Rainbow. According to his experience, he thought that Freda always said "lala." at the end of her sentences, while Rainbow always said "miao." at the beginning of his sentences. For each sentence in the chat record, help liouzhou_101 find whose sentence it is.

## Input

The first line of the input contains an integer n (1 ≤ n ≤ 10), number of sentences in the chat record. Each of the next n lines contains a sentence. A sentence is a string that contains only Latin letters (A-Z, a-z), underline (_), comma (,), point (.) and space ( ). Its length doesn’t exceed 100.

## Output

For each sentence, output "Freda's" if the sentence was said by Freda, "Rainbow's" if the sentence was said by Rainbow, or "OMG>.< I don't know!" if liouzhou_101 can’t recognize whose sentence it is. He can’t recognize a sentence if it begins with "miao." and ends with "lala.", or satisfies neither of the conditions.

## Sample 1

Input

```text
5
I will go to play with you lala.
wow, welcome.
miao.lala.
miao.
miao .
```

Output

```text
Freda's
OMG>.< I don't know!
OMG>.< I don't know!
Rainbow's
OMG>.< I don't know!
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
