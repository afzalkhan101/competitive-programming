<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>

# 8B · Obsession with Robots

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="dsa">DSA</span><span class="practice-tag">constructive algorithms</span><span class="practice-tag">graphs</span><span class="practice-tag">implementation</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/8/B) · Rating 1400

Time: 2.0 seconds · Memory: 64.0 MB

## Problem

The whole world got obsessed with robots,and to keep pace with the progress, great Berland's programmer Draude decided to build his own robot. He was working hard at the robot. He taught it to walk the shortest path from one point to another, to record all its movements, but like in many Draude's programs, there was a bug — the robot didn't always walk the shortest path. Fortunately, the robot recorded its own movements correctly. Now Draude wants to find out when his robot functions wrong. Heh, if Draude only remembered the map of the field, where he tested the robot, he would easily say if the robot walked in the right direction or not. But the field map was lost never to be found, that's why he asks you to find out if there exist at least one map, where the path recorded by the robot is the shortest.

The map is an infinite checkered field, where each square is either empty, or contains an obstruction. It is also known that the robot never tries to run into the obstruction. By the recorded robot's movements find out if there exist at least one such map, that it is possible to choose for the robot a starting square (the starting square should be empty) such that when the robot moves from this square its movements coincide with the recorded ones (the robot doesn't run into anything, moving along empty squares only), and the path from the starting square to the end one is the shortest.

In one movement the robot can move into the square (providing there are no obstrutions in this square) that has common sides with the square the robot is currently in.

## Input

The first line of the input file contains the recording of the robot's movements. This recording is a non-empty string, consisting of uppercase Latin letters L, R, U and D, standing for movements left, right, up and down respectively. The length of the string does not exceed 100.

## Output

In the first line output the only word OK (if the above described map exists), or BUG (if such a map does not exist).

## Sample 1

Input

```text
LLUUUR
```

Output

```text
OK
```

## Sample 2

Input

```text
RRUULLDD
```

Output

```text
BUG
```

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
