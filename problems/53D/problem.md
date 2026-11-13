# 53D · Physical Education

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">sortings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/53/D) · Rating 1500

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Vasya is a school PE teacher. Unlike other PE teachers, Vasya doesn't like it when the students stand in line according to their height. Instead, he demands that the children stand in the following order: a1, a2, ..., an, where ai is the height of the i-th student in the line and n is the number of students in the line. The children find it hard to keep in mind this strange arrangement, and today they formed the line in the following order: b1, b2, ..., bn, which upset Vasya immensely. Now Vasya wants to rearrange the children so that the resulting order is like this: a1, a2, ..., an. During each move Vasya can swap two people who stand next to each other in the line. Help Vasya, find the sequence of swaps leading to the arrangement Vasya needs. It is not required to minimize the number of moves.

## Input

The first line contains an integer n (1 ≤ n ≤ 300) which is the number of students. The second line contains n space-separated integers ai (1 ≤ ai ≤ 109) which represent the height of the student occupying the i-th place must possess. The third line contains n space-separated integers bi (1 ≤ bi ≤ 109) which represent the height of the student occupying the i-th place in the initial arrangement. It is possible that some students possess similar heights. It is guaranteed that it is possible to arrange the children in the required order, i.e. a and b coincide as multisets.

## Output

In the first line print an integer k (0 ≤ k ≤ 106) which is the number of moves. It is not required to minimize k but it must not exceed 106. Then print k lines each containing two space-separated integers. Line pi, pi + 1 (1 ≤ pi ≤ n - 1) means that Vasya should swap students occupying places pi and pi + 1.

## Sample 1

Input

```text
4
1 2 3 2
3 2 1 2
```

Output

```text
4
2 3
1 2
3 4
2 3
```

## Sample 2

Input

```text
2
1 100500
1 100500
```

Output

```text
0
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
