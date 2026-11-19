<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 490D · Chocolate

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">brute force</span><span class="practice-tag">dfs and similar</span><span class="practice-tag">math</span><span class="practice-tag">meet-in-the-middle</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/490/D) · Rating 1900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Polycarpus likes giving presents to Paraskevi. He has bought two chocolate bars, each of them has the shape of a segmented rectangle. The first bar is a1 × b1 segments large and the second one is a2 × b2 segments large.

Polycarpus wants to give Paraskevi one of the bars at the lunch break and eat the other one himself. Besides, he wants to show that Polycarpus's mind and Paraskevi's beauty are equally matched, so the two bars must have the same number of squares.

To make the bars have the same number of squares, Polycarpus eats a little piece of chocolate each minute. Each minute he does the following:

- he either breaks one bar exactly in half (vertically or horizontally) and eats exactly a half of the bar,
- or he chips of exactly one third of a bar (vertically or horizontally) and eats exactly a third of the bar.

In the first case he is left with a half, of the bar and in the second case he is left with two thirds of the bar.

Both variants aren't always possible, and sometimes Polycarpus cannot chip off a half nor a third. For example, if the bar is 16 × 23, then Polycarpus can chip off a half, but not a third. If the bar is 20 × 18, then Polycarpus can chip off both a half and a third. If the bar is 5 × 7, then Polycarpus cannot chip off a half nor a third.

What is the minimum number of minutes Polycarpus needs to make two bars consist of the same number of squares? Find not only the required minimum number of minutes, but also the possible sizes of the bars after the process.

## Input

The first line of the input contains integers a1, b1 (1 ≤ a1, b1 ≤ 109) — the initial sizes of the first chocolate bar. The second line of the input contains integers a2, b2 (1 ≤ a2, b2 ≤ 109) — the initial sizes of the second bar.

You can use the data of type int64 (in Pascal), long long (in С++), long (in Java) to process large integers (exceeding 231 - 1).

## Output

In the first line print m — the sought minimum number of minutes. In the second and third line print the possible sizes of the bars after they are leveled in m minutes. Print the sizes using the format identical to the input format. Print the sizes (the numbers in the printed pairs) in any order. The second line must correspond to the first bar and the third line must correspond to the second bar. If there are multiple solutions, print any of them.

If there is no solution, print a single line with integer -1.

## Sample 1

Input

```text
2 6
2 3
```

Output

```text
1
1 6
2 3
```

## Sample 2

Input

```text
36 5
10 16
```

Output

```text
3
16 5
5 16
```

## Sample 3

Input

```text
3 5
2 1
```

Output

```text
-1
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
