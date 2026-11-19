<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 53C · Little Frog

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/53/C) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Once upon a time a little frog whose name was Vasya decided to travel around his home swamp. Overall there are n mounds on the swamp, located on one line. The distance between the neighboring mounds is one meter. Vasya wants to visit all the mounds in one day; besides, he wants to visit each one exactly once. For that he makes a route plan, to decide the order in which to jump on the mounds. Vasya can pick any mound as the first one. He thinks it boring to jump two times at the same distance. That's why he wants any two jumps on his route to have different lengths. Help Vasya the Frog and make the plan for him.

## Input

The single line contains a number n (1 ≤ n ≤ 104) which is the number of mounds.

## Output

Print n integers pi (1 ≤ pi ≤ n) which are the frog's route plan.

- All the pi's should be mutually different.
- All the |pi–pi + 1|'s should be mutually different (1 ≤ i ≤ n - 1).

If there are several solutions, output any.

## Sample 1

Input

```text
2
```

Output

```text
1 2
```

## Sample 2

Input

```text
3
```

Output

```text
1 3 2
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
