# ia-solution-grad-problem
This is a solution repo for Impact Analysis Coding Question

## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

 
 Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

1. for 5 days: 14/29
2. for 10 days: 372/773

### How to execute?
```bash
python solution_grad_ceremony.py <N>
```
where N is the number of days untill graduation

### Solution Help

DP table for 5
```
A       N       Total
1       0       1
1       1       2
2       2       4
4       4       8
8       7       15
15      14      29
```

DP table for 10
```
A       N       Total
1       0       1
1       1       2
2       2       4
4       4       8
8       7       15
15      14      29
29      27      56
56      52      108
108     100     208
208     193     401
401     372     773

```
