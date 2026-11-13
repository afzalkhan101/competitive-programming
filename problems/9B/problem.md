# 9B · Running Student

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">brute force</span><span class="practice-tag">geometry</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/9/B) · Rating 1200

Time: 1.0 seconds · Memory: 64.0 MB

## Problem

And again a misfortune fell on Poor Student. He is being late for an exam.

Having rushed to a bus stop that is in point (0, 0), he got on a minibus and they drove along a straight line, parallel to axis OX, in the direction of increasing x.

Poor Student knows the following:

- during one run the minibus makes n stops, the i-th stop is in point (xi, 0)
- coordinates of all the stops are different
- the minibus drives at a constant speed, equal to vb
- it can be assumed the passengers get on and off the minibus at a bus stop momentarily
- Student can get off the minibus only at a bus stop
- Student will have to get off the minibus at a terminal stop, if he does not get off earlier
- the University, where the exam will be held, is in point (xu, yu)
- Student can run from a bus stop to the University at a constant speed vs as long as needed
- a distance between two points can be calculated according to the following formula: $$\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}$$
- Student is already on the minibus, so, he cannot get off at the first bus stop

Poor Student wants to get to the University as soon as possible. Help him to choose the bus stop, where he should get off. If such bus stops are multiple, choose the bus stop closest to the University.

## Input

The first line contains three integer numbers: 2 ≤ n ≤ 100, 1 ≤ vb, vs ≤ 1000. The second line contains n non-negative integers in ascending order: coordinates xi of the bus stop with index i. It is guaranteed that x1 equals to zero, and xn ≤ 105. The third line contains the coordinates of the University, integers xu and yu, not exceeding 105 in absolute value.

## Output

In the only line output the answer to the problem — index of the optimum bus stop.

## Sample 1

Input

```text
4 5 2
0 2 4 6
4 1
```

Output

```text
3
```

## Sample 2

Input

```text
2 1 1
0 100000
100000 100000
```

Output

```text
2
```

## Note

As you know, students are a special sort of people, and minibuses usually do not hurry. That's why you should not be surprised, if Student's speed is higher than the speed of the minibus.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
