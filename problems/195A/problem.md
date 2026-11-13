# 195A · Let's Watch Football

<!-- practice-tags:start -->
<div class="practice-tags" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="algorithms">Algorithms</span><span class="practice-tag">binary search</span><span class="practice-tag">brute force</span><span class="practice-tag">math</span></div>
<!-- practice-tags:end -->

[Codeforces problem](https://codeforces.com/problemset/problem/195/A) · Rating 1000

Time: 2.0 seconds · Memory: 256.0 MB

## Problem

Valeric and Valerko missed the last Euro football game, so they decided to watch the game's key moments on the Net. They want to start watching as soon as possible but the connection speed is too low. If they turn on the video right now, it will "hang up" as the size of data to watch per second will be more than the size of downloaded data per second.

The guys want to watch the whole video without any pauses, so they have to wait some integer number of seconds for a part of the video to download. After this number of seconds passes, they can start watching. Waiting for the whole video to download isn't necessary as the video can download after the guys started to watch.

Let's suppose that video's length is c seconds and Valeric and Valerko wait t seconds before the watching. Then for any moment of time t0, t ≤ t0 ≤ c + t, the following condition must fulfill: the size of data received in t0 seconds is not less than the size of data needed to watch t0 - t seconds of the video.

Of course, the guys want to wait as little as possible, so your task is to find the minimum integer number of seconds to wait before turning the video on. The guys must watch the video without pauses.

## Input

The first line contains three space-separated integers a, b and c (1 ≤ a, b, c ≤ 1000, a > b). The first number (a) denotes the size of data needed to watch one second of the video. The second number (b) denotes the size of data Valeric and Valerko can download from the Net per second. The third number (c) denotes the video's length in seconds.

## Output

Print a single number — the minimum integer number of seconds that Valeric and Valerko must wait to watch football without pauses.

## Sample 1

Input

```text
4 1 1
```

Output

```text
3
```

## Sample 2

Input

```text
10 3 2
```

Output

```text
5
```

## Sample 3

Input

```text
13 12 1
```

Output

```text
1
```

## Note

In the first sample video's length is 1 second and it is necessary 4 units of data for watching 1 second of video, so guys should download 4 · 1 = 4 units of data to watch the whole video. The most optimal way is to wait 3 seconds till 3 units of data will be downloaded and then start watching. While guys will be watching video 1 second, one unit of data will be downloaded and Valerik and Valerko will have 4 units of data by the end of watching. Also every moment till the end of video guys will have more data then necessary for watching.

In the second sample guys need 2 · 10 = 20 units of data, so they have to wait 5 seconds and after that they will have 20 units before the second second ends. However, if guys wait 4 seconds, they will be able to watch first second of video without pauses, but they will download 18 units of data by the end of second second and it is less then necessary.

---
Offline statement and original statement examples from [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.
