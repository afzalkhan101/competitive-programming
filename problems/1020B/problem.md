# 1020B · Badge

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/1020/B) · Rating 1000

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

In Summer Informatics School, if a student doesn't behave well, teachers make a hole in his badge. And today one of the teachers caught a group of $$$n$$$ students doing yet another trick.

Let's assume that all these students are numbered from $$$1$$$ to $$$n$$$. The teacher came to student $$$a$$$ and put a hole in his badge. The student, however, claimed that the main culprit is some other student $$$p_a$$$.

After that, the teacher came to student $$$p_a$$$ and made a hole in his badge as well. The student in reply said that the main culprit was student $$$p_{p_a}$$$.

This process went on for a while, but, since the number of students was finite, eventually the teacher came to the student, who already had a hole in his badge.

After that, the teacher put a second hole in the student's badge and decided that he is done with this process, and went to the sauna.

You don't know the first student who was caught by the teacher. However, you know all the numbers $$$p_i$$$. Your task is to find out for every student $$$a$$$, who would be the student with two holes in the badge if the first caught student was $$$a$$$.

## Input

The first line of the input contains the only integer $$$n$$$ ($$$1 \le n \le 1000$$$) — the number of the naughty students.

The second line contains $$$n$$$ integers $$$p_1$$$, ..., $$$p_n$$$ ($$$1 \le p_i \le n$$$), where $$$p_i$$$ indicates the student who was reported to the teacher by student $$$i$$$.

## Output

For every student $$$a$$$ from $$$1$$$ to $$$n$$$ print which student would receive two holes in the badge, if $$$a$$$ was the first student caught by the teacher.

## Sample 1

Input

```text
3
2 3 2
```

Output

```text
2 2 3
```

## Sample 2

Input

```text
3
1 2 3
```

Output

```text
1 2 3
```

## Note

The picture corresponds to the first example test case.

When $$$a = 1$$$, the teacher comes to students $$$1$$$, $$$2$$$, $$$3$$$, $$$2$$$, in this order, and the student $$$2$$$ is the one who receives a second hole in his badge.

When $$$a = 2$$$, the teacher comes to students $$$2$$$, $$$3$$$, $$$2$$$, and the student $$$2$$$ gets a second hole in his badge. When $$$a = 3$$$, the teacher will visit students $$$3$$$, $$$2$$$, $$$3$$$ with student $$$3$$$ getting a second hole in his badge.

For the second example test case it's clear that no matter with whom the teacher starts, that student would be the one who gets the second hole in his badge.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
