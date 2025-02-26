---
layout: post
title: Data Structures and Algorithms problems
tags: [Projects & coding skills]
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
<br/>
<br/>

# Problem 3: Longest Palindromic
##### Difficulty: Moderate
##### Date: 2020-02-20

## Problem statement
You will be given a string `s`, your job is to find and return the longest palindromic substring in `s`. 

#### Expected output
s = "babad"

Output : "bab" - even "aba" is a valid output

-----------------------------------------------
s = "cbbc"

Output : "bb"

## References
The problem is from [here](https://leetcode.com/problems/longest-palindromic-substring/)

#### End of problem statement

## Solution  
```python
def longestPalindrome(s):
    """
    The idea is to iterate and check through all possible combinations, **from the longest to the shortest**, and stop and return as soon as we find one (so that it's the longest one).
    """    
    for i in range(len(s),1,-1):
        for j in range(len(s)):
            if i%2 != 0:
                if (s[j:int((i-1)/2+j)] == s[int((i-1)/2+1+j):int(i+j)][::-1]):
                        return s[j:(i+j)]
            if i%2 == 0:
                if (s[j:int(i/2+j)] == s[int(i/2+j):(i+j)][::-1]):
                        return s[j:(i+j)]
    return 'no palindromic found'

def solution_two(s):
    """
    The idea is to iterate and check through all possible combinations, and return the longest palindrome.
    """    
    longest = ''
    for i in range(len(s),1,-1):
        for j in range(len(s)):
            n = s[j:(i+j)]
            if (n == n[::-1]):
                if len(n) > len(longest): # update the longest
                    longest = n
    return longest
```
<br/>
<br/>


# Problem 4: Even Fibonacci numbers
##### Difficulty: Easy
##### Date: 2020-02-22

## Problem statement
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


## References
The problem is from [here](https://projecteuler.net/problem=2)

#### End of problem statement

## Solution  
```python
def solution(limit = 4000000):
    s = 2
    m = 1
    n = 2
    x = 0
    while x <= limit:
        x = m+n
        if x%2 == 0:
            s+=x
        m = n
        n = x
    return s
```
<br/>
<br/>


# Problem 5: Largest prime factor
##### Difficulty: Moderate
##### Date: 2020-02-22

## Problem statement
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


## References
The problem is from [here](https://projecteuler.net/problem=3)

#### End of problem statement

## Solution  
```python
# the key in solving this problem is to realize that the combination of the prime factors is unique. 
def is_prime(s):
    mm = s-1
    while mm > 1:
        if s%mm == 0:
            return False
        mm -= 1
    return True

n = 1
x = 600851475143
while x != 1:
    n+=1
    while is_prime(n)==False:
        n+=1
    if x%n == 0:
        x = x/n
        print('factor',n)
print("largest prime factor is{}".format(n))
```
<br/>
<br/>



# Problem 6: Largest palindrome product
##### Difficulty: Easy
##### Date: 2020-02-22

## Problem statement
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


## References
The problem is from [here](https://projecteuler.net/problem=4)

#### End of problem statement

## Solution  
```python
x = 999
y = 999
largest = 0
while x>499:
    while y>1:
        n = x*y
        if str(n) == str(n)[::-1]:
            if n>largest:
                largest = n
                print(x,y,largest)
            break
        y-=1
    y=999
    x-=1
```
<br/>
<br/>



# Problem 7: Smallest multiple
##### Difficulty: Easy
##### Date: 2020-02-23

## Problem statement
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


## References
The problem is from [here](https://projecteuler.net/problem=5)

#### End of problem statement

## Solution  
```python
"""
if a number is evenly divisible by both 16 and 18, then it's ED by 12, because 16 and 18 contains 3 and 4 (4*4 * 3*6 = 3*4 * 4*6)
"""
def not_evenly_divisible_20(x):
    if sum(x%y for y in [20,19,18,17,16,15,14,13,11])==0:
        return False
    return True
    
x = 2520
while not_evenly_divisible_20(x):
    x+=20
x    
```
<br/>
<br/>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem 8: 10001st prime
##### Difficulty: Easy/Moderate
##### Date: 2020-02-24

## Problem statement
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


## References
The problem is from [here](https://projecteuler.net/problem=7)

#### End of problem statement

## Solution  
```python
def get_nth_prime(n):
    """
    The point here is: if a number `x` can't be evenly divided by any prime numbers that's smaller than `x`, then `x` is prime.
    """
    prime_list = [2] # initiate the list with the first prime number
    x = 3
    while len(prime_list) < n:
        prime = True
        for i in prime_list:
            if x % i == 0:
                prime = False
                x += 2 # even numbers>2 can't be prime
                break # we don't want to waste time checking the rest
        if prime:
            prime_list.append(x)
            x += 2
    return prime_list

get_nth_prime(10001)[-1]
```
<br/>
<br/>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem 9: Largest product in a series
##### Difficulty: Easy
##### Date: 2020-03-15

## Problem statement
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

`73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450`

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?



## References
The problem is from [here](https://projecteuler.net/problem=8)

#### End of problem statement

## Solution  
```python
n="""that very long string of number
"""

n = n.replace('\n', '')
n_proc = [x for x in n.split('0') if len(x) >=13]

p_max = 0
record = ''
for x in n_proc:
    
    for i in range(len(x)-12):
        slis = x[i: i+13]
        p = 1
        for e in slis:
            p *= int(e)
        if p > p_max:
            p_max,record = p,slis 
            
p_max, record
```
<br/>
<br/>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem 10: Special Pythagorean triplet
##### Difficulty: Easy
##### Date: 2020-03-24

## Problem statement
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,  

$$a^2 + b^2 = c^2$$

For example, $$3^2 + 4^2 = 5^2$$  

There exists exactly one Pythagorean triplet for which a + b + c = 1000.  
Find the product `abc`.  


## References
The problem is from [here](https://projecteuler.net/problem=9)

#### End of problem statement

## Solution  
```python
def not_pythagorean(a,b,c):
    if a**2 + b**2 == c**2:
        return False
    return True

a = 0
b = a
c = 1000 - a - b
while not_pythagorean(a,b,c) and a < c:
    a += 1
    b = a
    c = 1000 - a - b
    while not_pythagorean(a,b,c) and b < c:
        b += 1
        c = 1000 - a - b
print(a,b,c)

```
<br/>
<br/>

# Problem 11: Summation of primes
##### Difficulty: Easy
##### Date: 2020-04-19

## Problem statement
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  

Find the sum of all the primes below two million.


## References
The problem is from [here](https://projecteuler.net/problem=10)

#### End of problem statement

## Solution  
```python
def get_limit_prime(n):
    """
    The point here is: if a number `x` can't be evenly divided by any prime numbers that's smaller than `x`, then `x` is prime.
    """
    prime_list = [2] # initiate the list with the first prime number
    x = 3
    while x < n:
        prime = True
        for i in prime_list:
            if x % i == 0:
                prime = False
                x += 2 # even numbers>2 can't be prime
                break # we don't want to waste time checking the rest
        if prime:
            prime_list.append(x)
            x += 2
        # if x % 50000 == 1:
        #     print(x)
    return prime_list

n = 2000000
l = get_limit_prime(n)
sum(l)

```
<br/>
<br/>

# Problem 12: Largest product in a grid
##### Difficulty: Easy
##### Date: 2020-04-19

## Problem statement
In the 20×20 grid below, four numbers along a diagonal line have been marked in bold font.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08<br>
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00<br>
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65<br>
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91<br>
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80<br>
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50<br>
32 98 81 28 64 23 67 10 **26** 38 40 67 59 54 70 66 18 38 64 70<br>
67 26 20 68 02 62 12 20 95 **63** 94 39 63 08 40 91 66 49 94 21<br>
24 55 58 05 66 73 99 26 97 17 **78** 78 96 83 14 88 34 89 63 72<br>
21 36 23 09 75 00 76 44 20 45 35 **14** 00 61 33 97 34 31 33 95<br>
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92<br>
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57<br>
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58<br>
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40<br>
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66<br>
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69<br>
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36<br>
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16<br>
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54<br>
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48<br>

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

## References
The problem is from [here](https://projecteuler.net/problem=11)

#### End of problem statement

## Solution  
```python
data = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

ary = np.array([int(i) for i in data.split()])
dim = int(len(ary) ** 0.5)
shape = (dim, dim)
data = ary.reshape(shape)

# right/left 
for i in range(dim):
    for j in range(dim-4):
          p = 1
          for x in data[i, j:j+4]:
              p = p*x
          if p > p_l:
              p_l = p
# up/down
for i in range(dim-4):
    for j in range(dim):
          p = 1
          for x in data[i:i+4, j]:
              p = p*x
          if p > p_l:
              p_l = p
# diagonally
for i in range(dim-4):
    for j in range(dim-4):
        p = data[i, j]*data[i+1, j+1]*data[i+2, j+2]*data[i+3, j+3]
        if p > p_l:
            p_l = p
        p = data[i, j+3]*data[i+1, j+2]*data[i+2, j+1]*data[i+3, j]
        if p > p_l:
            p_l = p

print(p_l)

```
<br/>
<br/>


# Problem 13: Feature selection by correlation
##### Difficulty: Easy
##### Date: 2020-06-06

## Problem statement
This is a problem that I had in my current project. <br>
What needs to be done is to, given the `X` dataframe, drop the features that have high correlations (higher than `corr_bar`) and keep whichever has the higher Information Value (IV), according to the given `iv_df`.<br>
Notes:<br>
1. `X` contains missing values. 
2. `iv_df` = pd.DataFrame({"feature": [list_of_feature_names], "iv": [corresponding iv of the features]})
3. The function works like this: ftr_select_corr(X, corr_bar, iv_df)

## References
NA

#### End of problem statement

## Solution  
```python
def ftr_select_corr(X, corr_bar, iv_df):
    """
    Drop features that have correlation higher than `corr_bar` and keep whichever has the higher iv according to `iv_dif`.
    """

    cols = list(X.columns)
    cols_drop = []
    corr_df = X.corr()
#     print("corr_df created.")
    i = 0
    while i < len(cols) - 1:
        col_1 = cols[i]
        j = i + 1 
        while j < len(cols):
            col_2 = cols[j]
            corr = corr_df.loc[col_2, col_1]
            if abs(corr) > corr_bar:
                iv_1 = iv_df.query('feature == @col_1')['iv'].squeeze()
                iv_2 = iv_df.query('feature == @col_2')['iv'].squeeze()
                col_drop = col_2 if iv_1 > iv_2 else col_1
                cols_drop.append(col_drop)
                cols.remove(col_drop)
                X = X.drop(col_drop, axis=1)
                j -= 1
                if col_drop == col_1:
                    i -= 1
                    break
            j += 1
        i += 1
    return [X, cols_drop]

```
<br/>
<br/>


# Problem 14: Reducing Dishes
##### Difficulty: Easy
##### Date: 2020-06-06

## Problem statement
A chef has collected data on the `satisfaction` level of his `n` dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  `time[i]*satisfaction[i]`

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:<br>
>Input: satisfaction = [-1,-8,0,5,-9]<br>
>Output: 14<br>
>Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.<br>

Example 2:<br>
>Input: satisfaction = [4,3,2]<br>
>Output: 20<br>
>Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)<br>

Example 3:<br>
>Input: satisfaction = [-1,-4,-5]<br>
>Output: 0<br>
>Explanation: People don't like the dishes. No dish is prepared.<br>

Example 4:<br>
>Input: satisfaction = [-2,5,-1,0,3,-3]<br>
>Output: 35<br>
 

Constraints:<br>
>n == satisfaction.length<br>
>1 <= n <= 500<br>
>-10^3 <= satisfaction[i] <= 10^3<br>


## References
The problem is from [here](https://leetcode.com/problems/reducing-dishes/)

#### End of problem statement

## Solution  
```python
def maxSatisfaction(satisfaction):
    """
    Early stopping could be added to make the method more efficient.
    """
        max_coef = 0
        best_combo = []
        satisfaction_sorted = sorted(satisfaction)

        for n in range(1, len(satisfaction)+1):
            coef = sum([satisfaction_sorted[-n:][i] * (i+1) for i in range(n)])
            if coef > max_coef:
                max_coef = coef
                best_combo = satisfaction_sorted[-n:]
        
        return max_coef

```
<br/>
<br/>
