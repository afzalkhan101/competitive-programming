# 427B · Prison Transfer

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">data structures</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/427/B) · Rating 1100

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

The prison of your city has n prisoners. As the prison can't accommodate all of them, the city mayor has decided to transfer c of the prisoners to a prison located in another city.

For this reason, he made the n prisoners to stand in a line, with a number written on their chests. The number is the severity of the crime he/she has committed. The greater the number, the more severe his/her crime was.

Then, the mayor told you to choose the c prisoners, who will be transferred to the other prison. He also imposed two conditions. They are,

- The chosen c prisoners has to form a contiguous segment of prisoners.
- Any of the chosen prisoner's crime level should not be greater then t. Because, that will make the prisoner a severe criminal and the mayor doesn't want to take the risk of his running away during the transfer.

Find the number of ways you can choose the c prisoners.

## Input

The first line of input will contain three space separated integers n (1 ≤ n ≤ 2·105), t (0 ≤ t ≤ 109) and c (1 ≤ c ≤ n). The next line will contain n space separated integers, the ith integer is the severity ith prisoner's crime. The value of crime severities will be non-negative and will not exceed 109.

## Output

Print a single integer — the number of ways you can choose the c prisoners.

## Sample 1

Input

```text
4 3 3
2 3 1 1
```

Output

```text
2
```

## Sample 2

Input

```text
1 1 1
2
```

Output

```text
0
```

## Sample 3

Input

```text
11 4 2
2 2 0 7 3 2 2 4 9 1 4
```

Output

```text
6
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
