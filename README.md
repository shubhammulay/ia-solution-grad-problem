# ia-solution-grad-problem
This is a solution repo for Impact Analysis Coding Question

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