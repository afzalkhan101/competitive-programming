<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 70B · Text Messaging

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">expression parsing</span><span class="practice-tag">greedy</span><span class="practice-tag">strings</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/70/B) · Rating 1600

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Fangy the little walrus, as all the modern walruses, loves to communicate via text messaging. One day he faced the following problem: When he sends large texts, they are split into parts each containing n characters (which is the size of one text message). Thus, whole sentences and words get split!

Fangy did not like it, so he faced the task of breaking the text into minimal messages on his own so that no sentence were broken into pieces when it is sent and the number of text messages to be sent would be minimal. If two consecutive sentences are in different messages, the space between them can be ignored (Fangy does not write this space).

The little walrus's text looks in the following manner:

SPACE stands for the symbol of a space.

So, how many messages did Fangy send?

## Input

The first line contains an integer n, which is the size of one message (2 ≤ n ≤ 255). The second line contains the text. The length of the text does not exceed 104 characters. It is guaranteed that the text satisfies the above described format. Specifically, this implies that the text is not empty.

## Output

On the first and only line print the number of text messages Fangy will need. If it is impossible to split the text, print "Impossible" without the quotes.

## Sample 1

Input

```text
25
Hello. I am a little walrus.
```

Output

```text
2
```

## Sample 2

Input

```text
2
How are you?
```

Output

```text
Impossible
```

## Sample 3

Input

```text
19
Hello! Do you like fish? Why?
```

Output

```text
3
```

## Note

Let's take a look at the third sample. The text will be split into three messages: "Hello!", "Do you like fish?" and "Why?".

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
