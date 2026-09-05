# Task 0

Name: Esh

My submission for Task 0. It covers the basic Python questions (Q1 to Q3) and then the small data pipeline with NumPy, Pandas and Matplotlib (Q4 to Q6).

## Files

```
task-0/
  q1.py to q6.py
  data/student_performance.csv              (given with the task)
  data/processed_student_performance.csv    (made by q5.py)
  plots/                                    (4 images made by q6.py)
  requirements.txt
```

## Setup

You need Python 3 and the three libraries below.

```
pip install -r requirements.txt
```

Q1, Q2 and Q3 don't need any libraries, only Q4 to Q6 do.

## How to run

Run everything from inside the task-0 folder, otherwise the csv path won't be found.

```
python q1.py     (type N, then the numbers on the next line)
python q2.py
python q3.py     (type N, like 20)
python q4.py
python q5.py
python q6.py
```

Run q5.py before q6.py because q6 reads the processed file that q5 creates.

## Notes

For Q1 I did the largest, smallest and sum with a single loop and comparisons, and reversed the list by looping backwards from the last index, so no max, min, sum or sort anywhere.

In Q2 I first tried removing the negatives inside the same loop and it skipped some numbers, since the list shifts while you are looping over it. So now I collect the negatives in a separate list first and then remove them.

The comment about for-else is inside q3.py. Short version is that the else block runs only when the loop ends without hitting a break.

For Q4 I picked 10 students from the csv and typed the values in directly since the question said the csv shouldn't be read yet. Only one of them is above 75 because the marks in this dataset are quite low overall.

## What I noticed in the data

There are 80 students and no missing values. The average final score is 47.89 and the lowest is 35, which shows up a lot of times, so 35 seems to be the minimum mark they give.

Hours studied is clearly the thing that matters most, you can see it in the scatter plot going up from left to right. I made my extra plot attendance vs final score to compare, and that one is basically a cloud with no pattern, so attendance alone doesn't do much.
