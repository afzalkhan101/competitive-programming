<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 44H · Phone Number

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">dp</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/44/H) · Rating 1700

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Alas, finding one's true love is not easy. Masha has been unsuccessful in that yet. Her friend Dasha told Masha about a way to determine the phone number of one's Prince Charming through arithmancy.

The phone number is divined like that. First one needs to write down one's own phone numbers. For example, let's suppose that Masha's phone number is 12345. After that one should write her favorite digit from 0 to 9 under the first digit of her number. That will be the first digit of the needed number. For example, Masha's favorite digit is 9. The second digit is determined as a half sum of the second digit of Masha's number and the already written down first digit from her beloved one's number. In this case the arithmetic average equals to (2 + 9) / 2 = 5.5. Masha can round the number up or down, depending on her wishes. For example, she chooses the digit 5. Having written down the resulting digit under the second digit of her number, Masha moves to finding the third digit in the same way, i.e. finding the half sum the the third digit of her number and the second digit of the new number. The result is (5 + 3) / 2 = 4. In this case the answer is unique. Thus, every i-th digit is determined as an arithmetic average of the i-th digit of Masha's number and the i - 1-th digit of her true love's number. If needed, the digit can be rounded up or down. For example, Masha can get:

12345

95444

## Input

The first line contains nonempty sequence consisting of digits from 0 to 9 — Masha's phone number. The sequence length does not exceed 50.

## Output

Output the single number — the number of phone numbers Masha will dial.

## Sample 1

Input

```text
12345
```

Output

```text
48
```

## Sample 2

Input

```text
09
```

Output

```text
15
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
