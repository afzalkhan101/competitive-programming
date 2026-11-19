<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 822A · I'm bored with life

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="number-theory">Number Theory</span><span class="practice-tag">implementation</span><span class="practice-tag">math</span><span class="practice-tag">number theory</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/822/A) · Rating 800

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Holidays have finished. Thanks to the help of the hacker Leha, Noora managed to enter the university of her dreams which is located in a town Pavlopolis. It's well known that universities provide students with dormitory for the period of university studies. Consequently Noora had to leave Vičkopolis and move to Pavlopolis. Thus Leha was left completely alone in a quiet town Vičkopolis. He almost even fell into a depression from boredom!

Leha came up with a task for himself to relax a little. He chooses two integers A and B and then calculates the greatest common divisor of integers "A factorial" and "B factorial". Formally the hacker wants to find out GCD(A!, B!). It's well known that the factorial of an integer x is a product of all positive integers less than or equal to x. Thus x! = 1·2·3·...·(x - 1)·x. For example 4! = 1·2·3·4 = 24. Recall that GCD(x, y) is the largest positive integer q that divides (without a remainder) both x and y.

Leha has learned how to solve this task very effective. You are able to cope with it not worse, aren't you?

## Input

The first and single line contains two integers A and B (1 ≤ A, B ≤ 109, min(A, B) ≤ 12).

## Output

Print a single integer denoting the greatest common divisor of integers A! and B!.

## Sample 1

Input

```text
4 3
```

Output

```text
6
```

## Note

Consider the sample.

4! = 1·2·3·4 = 24. 3! = 1·2·3 = 6. The greatest common divisor of integers 24 and 6 is exactly 6.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
