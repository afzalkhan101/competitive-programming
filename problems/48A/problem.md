# 48A · Rock-paper-scissors

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="basics">Basics</span><span class="practice-tag">implementation</span><span class="practice-tag">schedules</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/48/A) · Rating 900

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Uncle Fyodor, Matroskin the Cat and Sharic the Dog live their simple but happy lives in Prostokvashino. Sometimes they receive parcels from Uncle Fyodor’s parents and sometimes from anonymous benefactors, in which case it is hard to determine to which one of them the package has been sent. A photographic rifle is obviously for Sharic who loves hunting and fish is for Matroskin, but for whom was a new video game console meant? Every one of the three friends claimed that the present is for him and nearly quarreled. Uncle Fyodor had an idea how to solve the problem justly: they should suppose that the console was sent to all three of them and play it in turns. Everybody got relieved but then yet another burning problem popped up — who will play first? This time Matroskin came up with a brilliant solution, suggesting the most fair way to find it out: play rock-paper-scissors together. The rules of the game are very simple. On the count of three every player shows a combination with his hand (or paw). The combination corresponds to one of three things: a rock, scissors or paper. Some of the gestures win over some other ones according to well-known rules: the rock breaks the scissors, the scissors cut the paper, and the paper gets wrapped over the stone. Usually there are two players. Yet there are three friends, that’s why they decided to choose the winner like that: If someone shows the gesture that wins over the other two players, then that player wins. Otherwise, another game round is required. Write a program that will determine the winner by the gestures they have shown.

## Input

The first input line contains the name of the gesture that Uncle Fyodor showed, the second line shows which gesture Matroskin showed and the third line shows Sharic’s gesture.

## Output

Print "F" (without quotes) if Uncle Fyodor wins. Print "M" if Matroskin wins and "S" if Sharic wins. If it is impossible to find the winner, print "?".

## Sample 1

Input

```text
rock
rock
rock
```

Output

```text
?
```

## Sample 2

Input

```text
paper
rock
rock
```

Output

```text
F
```

## Sample 3

Input

```text
scissors
rock
rock
```

Output

```text
?
```

## Sample 4

Input

```text
scissors
paper
rock
```

Output

```text
?
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
