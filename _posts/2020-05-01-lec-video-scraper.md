---
layout: post
title: Scrape, rename and sort lecture recordings by course
tags: [Coding Practice]
excerpt_separator: <!--more-->
---

Made a simple scraper to download all the lecture recordings. Then rename and sort them by courses. <br>

<!--more-->
## Code
```python
# Python3

import requests
from bs4 import BeautifulSoup
import wget
import os

################
### Download ###
################
# download all the lecture recordings from "http://"

url = "http://"
rq = requests.get(url)
bs = BeautifulSoup(rq.text, features="lxml")
mp4 = [x.text for x in bs.find_all("li")]
t = len(mp4)

print("Download start.\n{} videos in total.\n".format(t))
n = 1

for m in mp4:
    url_dl = url+m
    print("[{}/{}] {}".format(n, t, m))
    wget.download(url_dl)
    print()
    n += 1

print("\nDownload finished\n")



################
#### Rename ####
################
# rename files
# e.g. `20190909-090006-008.mp4` to `521-1.mp4`.

id_seq = [[521, 551, 542, 511], [531, 552, 512, 523], [561, 571, 532, 513], [562, 572, 573, 522], [563, 524, 574, 553]] # lecture sequence based on calendar
file_names = []
for x in id_seq:
    for i in range(1, 9):
        file_names.extend(str(y)+'-'+str(i) for y in x)

# HANDLE EXCEPTIONS:
# 2019-10-18 missing : '531-2', '552-2'
# 2019-10-24 one lecture (523) missing: '523-4'
# 2020-01-17 missing: '562-2', '572-2'
# final week missing (2020-03-16 ~ 2020-03-19): [563, 524, 574, 553] - 7&8
miss_rec = ['531-2', '552-2', '523-4', '562-2', '572-2', '563-7', '524-7', '574-7', '553-7', '563-8', '524-8', '574-8', '553-8']

file_names = [x for x in file_names if x not in miss_rec] # drop missing records

i = file_names.index('531-1')
file_names[i: i+4] = ['512-1', '523-1', '531-1', '552-1'] # course order is different in that week

print("Renaming files:\n")
i = 0
log = []
for x in os.listdir():
    if x[-4:] == '.mp4': 
        os.rename(x, file_names[i]+'.mp4')
        rec = x+' to '+file_names[i]+'.mp4'
        print(rec)
        log.append(rec)
        i += 1

# save the rename log in a text file
f = open('rename_log.txt','w')
for ele in log:
    f.write(ele+'\n')

f.close()

# save the missing recordings
f = open('missing_recordings.txt','w')
for ele in miss_rec:
    f.write(ele+'\n')

f.close()


print('\nRenaming completed. Log saved as `rename_log.txt` and `missing_recordings.txt`.')



################
#### Folder ####
################
# create folders by course and move recordings into folders accordingly
# e.g.: `551-1.mp4` moved into `DSCI_551_Descriptive Statistics and Probability for Data Science`


# get the course ID and names to create folders
# course_html = requests.get("https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept=DSCI")
course_html = requests.get("https://courses.students.ubc.ca/cs/courseschedule?tname=subj-department&sessyr=2020&sesscd=W&dept=DSCI&pname=subjarea")

course_bs = BeautifulSoup(course_html.text, features="lxml")
l = [x.text for x in course_bs.find_all('td')][2: -4]

id_name_dict = {}
id_list = l[::2]
id_list = [x.replace(" ", "_") for x in id_list]
name_list = l[1::2]
# name_list = [x.replace(" ", "-") for x in name_list]
for i in range(int(len(l)/2)):
    full_name = id_list[i]+'_'+name_list[i]
    id_name_dict[id_list[i][-3:]] = full_name

    
# create folders for each course
for x in id_name_dict.values():
    os.mkdir(x)

# move recordings into the folders they belong
print("\nMoving files into folders: \n")
log = []
for x in os.listdir():
    if x[-4:] == '.mp4':
        os.rename(x, str(id_name_dict[x[:3]])+'/'+x)
        rec = str(x)+' moved into '+str(id_name_dict[x[:3]])
        print(rec)
        log.append(rec)

# save the log in a text file
f = open('folderize_log.txt','w')
for ele in log:
    f.write(ele+'\n')

f.close()

print('\nCompleted. Log saved as `folderize_log.txt`.')

```
