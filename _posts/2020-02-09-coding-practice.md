---
layout: post
title: Data Structures and Algorithms problems
tags: [Coding Practice]
excerpt_separator: <!--more-->
---
Data Structures and Algorithms problems solving practices. Continuously updating (hopefully every week).
<!--more-->

# Problem 1: Spiral Matrix
##### Difficulty: Difficult
##### Date: 2020-02-09

## Problem statement
You will be given a positive integer input N, and your job is to return a spiral matrix list size of NxN. 

#### Constraints
N >= 1

#### Expected output

N = 2

Expected output = 

[[1, 2],

[4, 3]]

--------------------------

N = 3 

Expected output = 

[[1, 2, 3],

[8, 9, 4],

[7, 6, 5]]

#### End of problem statement

## Solution  

```python
def solution(n):

    # Finding the right way to initialize `x` took me almost as much time as solving the rest of the problem orz
    # I started initializing with x = [[0] * n ] * n, but funny things would happen
    x = [[0 for x in range(n)] for y in range(n)] 

    stop = n**2
    m  = 1 # numbers 12345678...stop 
    r = 0 # round

    # fill in the numbers one by one brutally
    while m <= stop:
        # go right
        for i in range(r, n-r):
            x[r][i] = m
            m+=1
        # go down
        for i in range(r+1, n-r):
            x[i][n-r-1] = m
            m+=1
        # go left
        for i in range(n-r-2, r-1, -1):
            x[n-r-1][i] = m
            m+=1
        # go up
        for i in range(n-r-2, r, -1):
            x[i][r] = m
            m+=1
        # next round
        r+=1
        
    return x
```
<br/>
<br/>

# Problem 2: Pyramid
##### Difficulty: Moderate
##### Date: 2020-02-17

## Problem statement
You will be given an integer input N and your job is to append to a list a pyramid with exactly that many levels.

#### Expected output: list

Input: N = 2

Please note that the `-` are **not** a part of the output, only to show you that a **space** is required.

Output:

(below is for readability, output should be of the format: [" # ", "###"])

'-#-'

'###'

Input: N = 3

'--#--'

'-###-'

'#####'

## Constraints

Input will be positive integer.

#### End of problem statement

## Solution  
```python

def solution(N):
    return [' '*(N-i-1) + '#'*(2*i+1) + ' '*(N-i-1) for i in range(N)]

```