<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 72E · Ali goes shopping

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="mixed">Mixed Practice</span><span class="practice-tag">*special</span><span class="practice-tag">brute force</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/72/E) · Rating 1800

Time: 5.0 seconds · Memory: 256.0 MB

## Problem

Ali Koochooloo is going to buy new clothes since we're reaching Noruz, the ancient Persian festival and the beginning of new Persian year.

When Ali entered a shop, he saw that the shopkeeper was a programmer and since there is no money in programming he had changed his career. The shopkeeper told Ali that he can buy anything for free if he could answer a simple question in 10 seconds. But to see the question Ali has to pay 3 tomans.

Ali agreed instantly and the shopkeeper handed him a piece of paper containing the task. The task was indeed very simple. It said:

Let string A be ababababababab. Which non-empty substring of A is repeated the most times in it?

Ali answered fast. He said the answer is a. But the shopkeeper said that Ali is wrong and asked him to read the rest of statement:

If several substrings have the maximal repeat time, then the substring with maximal length would be the answer, in case of a tie the alphabetically latest substring will be chosen.

So the answer is ab.

Now Ali wants us to solve this problem for different strings. We don't have a great advantage over Ali, we just have a computer and a weird language.

## Input

The single line consisting of a string A. It is non-empty, made of lower-case Latin letters and contains at most 30 characters.

## Output

The single line contains the answer.

## Sample 1

Input

```text
abab
```

Output

```text
ab
```

## Sample 2

Input

```text
abcd
```

Output

```text
abcd
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
