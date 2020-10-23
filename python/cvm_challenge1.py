#!/usr/bin/env python3

"""
    Python 3 Code Challenge by Jim Briante

    Implemented in python3 by Craig Miller 1 Oct 2020
    Version 0.90
"""

#
# Globals
#
input_list = [72,111,63,85,61,56,118,121,61,69,63,61]

#1
input_total = sum(input_list)
print("Output1: Sum is:%s" % (input_total))

#2
input_avg = int(input_total / 12)
input_remainder = input_total % 12

print("Output2: Avg:%s Remainder is:%s" % (input_avg,input_remainder))

#3

input_even=[]
for i in input_list:
    if (i % 2 == 0):
        input_even.append(i)

print("Output3: even values are: %s" % input_even)

#4
pos = 0
lpos = 0
for i in input_list:
    if pos == 0 :
        lmin = i
    elif lmin > i:
        lmin = i
        lpos = pos
    pos += 1

print("Output4: min is: %s position is: %s" % (lmin, lpos))

#5 - still needs work
# use numpy
import numpy
dup_list = []
sort_list = sorted(input_list)
last_value = 0
for i in sort_list:
    if i == last_value :
        dup_list.append(i)
    else:
        last_value = i

print("Output5: Duplicates %s" % (dup_list))

#6
hibits = input_list[0]
lobits = input_list[1]
sixteen_bits = hibits * 256 + lobits
print("Output6: 16 bit number %s" % sixteen_bits)

#7

print("Output7: sorted list %s" % sort_list)

#8
char_str = ''
char_list = []
for i in input_list:
    char_list.append(chr(i))
char_str = char_str.join(char_list)
print("Output8: character list %s" % char_str)

#9 Upper case
up_str = ""
for i in char_list:
    if (ord(i) > 64 and ord(i) < 91) or (ord(i) > 97 and ord(i) < 123):
        up_str = up_str + i.upper()

print("Output9: character list %s" % up_str)

#10 coded word key

coded_word = "BIOPSY"
plain_word = up_str
coded_key = ord(plain_word[1]) - ord(coded_word[1])

print("Output10: coded word key %s" % coded_key)


print("Pau")