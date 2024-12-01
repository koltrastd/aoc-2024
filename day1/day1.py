#!/usr/bin/env python3

import re

file=open("input.txt","r")

# Declare lists/dicts
list1=[]
list2=[]
list_diff=[]
dict_similar={}
score_list=[]

# Populate lists
lines=file.readlines()
for line in lines:
  groups = re.search(r'(^[0-9]+)\s+([0-9]+)', line)
  list1.append(int(groups.group(1)))
  list2.append(int(groups.group(2)))

list1.sort()
list2.sort()

# Task 1
for idx,idy in enumerate(list1):
  if idy > list2[idx]:
    list_diff.append(idy-list2[idx])
  else:
    list_diff.append(list2[idx]-idy)
 
# Task 2 
  if idy in list2:
    if idy not in dict_similar: 
      dict_similar.update({idy: list2.count(idy)})

for value, occurance in dict_similar.items():
    score_list.append(int(value) * int(occurance))

print(f"Distance: {sum(list_diff)}")
print(f"Similarity Score: {sum(score_list)}")


