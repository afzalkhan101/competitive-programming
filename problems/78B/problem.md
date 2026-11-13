# 78B · Easter Eggs

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/78/B) · Rating 1200

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

The Easter Rabbit laid n eggs in a circle and is about to paint them.

Each egg should be painted one color out of 7: red, orange, yellow, green, blue, indigo or violet. Also, the following conditions should be satisfied:

- Each of the seven colors should be used to paint at least one egg.
- Any four eggs lying sequentially should be painted different colors.

Help the Easter Rabbit paint the eggs in the required manner. We know that it is always possible.

## Input

The only line contains an integer n — the amount of eggs (7 ≤ n ≤ 100).

## Output

Print one line consisting of n characters. The i-th character should describe the color of the i-th egg in the order they lie in the circle. The colors should be represented as follows: "R" stands for red, "O" stands for orange, "Y" stands for yellow, "G" stands for green, "B" stands for blue, "I" stands for indigo, "V" stands for violet.

If there are several answers, print any of them.

## Sample 1

Input

```text
8
```

Output

```text
ROYGRBIV
```

## Sample 2

Input

```text
13
```

Output

```text
ROYGBIVGBIVYG
```

## Note

The way the eggs will be painted in the first sample is shown on the picture:

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
