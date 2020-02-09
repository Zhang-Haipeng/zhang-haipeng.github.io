---
layout: post
title: Data Structures and Algorithms problems
tags: [coding_practice, Projects]
excerpt_separator: <!--more-->
---

Data Structures and Algorithms coding practices. Continuously updating (hopefully every week).
<!--more-->

# Spiral Matrix
##### Difficulty: Difficult

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

## Solution  

```yml

def my_solution(n):

    # Finding the right way to initialize `x` took me almost as much time as solving the rest of the problem orz
    # I started initializing with x = [[0] * n ] * n, but funny things would happen
    x = [[0 for x in range(n)] for y in range(n)] 

    stop = n**2
    m  = 1 # the 12345678...stop 
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