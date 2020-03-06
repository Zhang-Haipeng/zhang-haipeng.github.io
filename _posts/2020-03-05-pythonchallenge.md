---
layout: post
title: pythonchallenge_com
tags: [Coding Practice]
excerpt_separator: <!--more-->
---
Record of solving [`pythonchallenge.com`](pythonchallenge.com).
<!--more-->

# Level 1

## code
```python
2**38
```
## solution
http://www.pythonchallenge.com/pc/def/274877906944.html

<br/>
<br/>

# Level 2

## code
```python
code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def solution(code=code):
    crack = ''
    for x in code:
        if (ord(x) > ord('a')) & (ord(x) < ord('y')):
            crack += chr(ord(x)+2)
        elif x == 'y':
            crack += 'a'
        elif x == 'z':
            crack += 'b'
        else:
            crack += x
    return crack

solution()
>>> "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."

solution("http://www.pythonchallenge.com/pc/def/map.html")
>>> "jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon"
```
## solution
http://www.pythonchallenge.com/pc/def/ocr.html


<br/>
<br/>


# Level 3

## solution  
* google "page source"  
* found website to view page source of websites, https://www.view-page-source.com/
* found the code to crack with
* split the code into a loooong list
* pd.DataFrame(list).unique() -- noticed there are letters hidden in the code : e q u a l i t y

<br/>
<br/>

# Level 4

## solution  
* Apparently "little candle" is not the answer.  
* Checking out the page source again and found the code.  
* Apparently, it's requiring regular expression. 
* I hate regular expression. So I tried 'a-z'. But disappointingly, it didn't work.  

## code  
```python
code = "the looong code"
crack =[]
cracker = ''
# the following code shows how much I hate regular expression
for i in range(1, len(code)-6):
    if ord(code[i-1]) >= ord('a'):
        if ord(code[i]) <= ord('Z'):
            if ord(code[i+1]) <= ord('Z'):
                if ord(code[i+2]) <= ord('Z'):
                    if ord(code[i+3]) >= ord('a'):
                        if ord(code[i+4]) <= ord('Z'):
                            if ord(code[i+5]) <= ord('Z'):
                                if ord(code[i+6]) <= ord('Z'):
                                    if ord(code[i+7]) >= ord('a'):
                                        if '\n' not in code[i:i+7]:
                                            crack.append(code[i-1:i+8])
                                            cracker += code[i+3]
                                    continue
                                continue
                            continue
                        continue
                    continue
                continue
            continue
        continue
        
crack,cracker

>>> (['qIQNlQSLi',
  'eOEKiVEYj',
  'aZADnMCZq',
  'bZUTkLYNg',
  'uCNDeHSBj',
  'kOIXdKBFh',
  'dXJVlGZVm',
  'gZAGiLQZx',
  'vCJAsACFl',
  'qKWGtIDCj'],
 'linkedlist')

```


<br/>
<br/>
