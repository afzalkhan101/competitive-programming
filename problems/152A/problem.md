<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 152A · Marks

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/152/A) · Rating 900

Time: 1.0 seconds · Memory: 256.0 MB

## Problem

Vasya, or Mr. Vasily Petrov is a dean of a department in a local university. After the winter exams he got his hands on a group's gradebook.

Overall the group has n students. They received marks for m subjects. Each student got a mark from 1 to 9 (inclusive) for each subject.

Let's consider a student the best at some subject, if there is no student who got a higher mark for this subject. Let's consider a student successful, if there exists a subject he is the best at.

Your task is to find the number of successful students in the group.

## Input

The first input line contains two integers n and m (1 ≤ n, m ≤ 100) — the number of students and the number of subjects, correspondingly. Next n lines each containing m characters describe the gradebook. Each character in the gradebook is a number from 1 to 9. Note that the marks in a rows are not sepatated by spaces.

## Output

Print the single number — the number of successful students in the given group.

## Sample 1

Input

```text
3 3
223
232
112
```

Output

```text
2
```

## Sample 2

Input

```text
3 5
91728
11828
11111
```

Output

```text
3
```

## Note

In the first sample test the student number 1 is the best at subjects 1 and 3, student 2 is the best at subjects 1 and 2, but student 3 isn't the best at any subject.

In the second sample test each student is the best at at least one subject.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
