# 129B · Students and Shoelaces

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">graphs</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/129/B) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Anna and Maria are in charge of the math club for junior students. When the club gathers together, the students behave badly. They've brought lots of shoe laces to the club and got tied with each other. Specifically, each string ties together two students. Besides, if two students are tied, then the lace connects the first student with the second one as well as the second student with the first one.

To restore order, Anna and Maria do the following. First, for each student Anna finds out what other students he is tied to. If a student is tied to exactly one other student, Anna reprimands him. Then Maria gathers in a single group all the students who have been just reprimanded. She kicks them out from the club. This group of students immediately leaves the club. These students takes with them the laces that used to tie them. Then again for every student Anna finds out how many other students he is tied to and so on. And they do so until Anna can reprimand at least one student.

Determine how many groups of students will be kicked out of the club.

## Input

The first line contains two integers n and m — the initial number of students and laces ($$1 \leq n \leq 100, 0 \leq m \leq \frac{n(n-1)}{2}$$). The students are numbered from 1 to n, and the laces are numbered from 1 to m. Next m lines each contain two integers a and b — the numbers of students tied by the i-th lace (1 ≤ a, b ≤ n, a ≠ b). It is guaranteed that no two students are tied with more than one lace. No lace ties a student to himself.

## Output

Print the single number — the number of groups of students that will be kicked out from the club.

## Sample 1

Input

```text
3 3
1 2
2 3
3 1
```

Output

```text
0
```

## Sample 2

Input

```text
6 3
1 2
2 3
3 4
```

Output

```text
2
```

## Sample 3

Input

```text
6 5
1 4
2 4
3 4
5 4
6 4
```

Output

```text
1
```

## Note

In the first sample Anna and Maria won't kick out any group of students — in the initial position every student is tied to two other students and Anna won't be able to reprimand anyone.

In the second sample four students are tied in a chain and two more are running by themselves. First Anna and Maria kick out the two students from both ends of the chain (1 and 4), then — two other students from the chain (2 and 3). At that the students who are running by themselves will stay in the club.

In the third sample Anna and Maria will momentarily kick out all students except for the fourth one and the process stops at that point. The correct answer is one.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
