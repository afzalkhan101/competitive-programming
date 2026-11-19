<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 62A · A Student's Dream

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">greedy</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/62/A) · Rating 1300

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Statistics claims that students sleep no more than three hours a day. But even in the world of their dreams, while they are snoring peacefully, the sense of impending doom is still upon them.

A poor student is dreaming that he is sitting the mathematical analysis exam. And he is examined by the most formidable professor of all times, a three times Soviet Union Hero, a Noble Prize laureate in student expulsion, venerable Petr Palych.

The poor student couldn't answer a single question. Thus, instead of a large spacious office he is going to apply for a job to thorium mines. But wait a minute! Petr Palych decided to give the student the last chance! Yes, that is possible only in dreams.

So the professor began: "Once a Venusian girl and a Marsian boy met on the Earth and decided to take a walk holding hands. But the problem is the girl has al fingers on her left hand and ar fingers on the right one. The boy correspondingly has bl and br fingers. They can only feel comfortable when holding hands, when no pair of the girl's fingers will touch each other. That is, they are comfortable when between any two girl's fingers there is a boy's finger. And in addition, no three fingers of the boy should touch each other. Determine if they can hold hands so that the both were comfortable."

The boy any the girl don't care who goes to the left and who goes to the right. The difference is only that if the boy goes to the left of the girl, he will take her left hand with his right one, and if he goes to the right of the girl, then it is vice versa.

## Input

The first line contains two positive integers not exceeding 100. They are the number of fingers on the Venusian girl's left and right hand correspondingly. The second line contains two integers not exceeding 100. They are the number of fingers on the Marsian boy's left and right hands correspondingly.

## Output

Print YES or NO, that is, the answer to Petr Palych's question.

## Sample 1

Input

```text
5 1
10 5
```

Output

```text
YES
```

## Sample 2

Input

```text
4 5
3 3
```

Output

```text
YES
```

## Sample 3

Input

```text
1 2
11 6
```

Output

```text
NO
```

## Note

The boy and the girl don't really care who goes to the left.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
