---
title: Use true random numbers in python.
tags: Python Terminal Random Linux module
author: fygar256
slide: false
---
This is a python module that extracts true random numbers.

There are two types of random numbers that can be used by computers: pseudorandom numbers with a period, and true random numbers that are statistically correct. There are also "completely random numbers" that cannot be handled by computers, and they can only be handled probabilistically. In other words, completely random numbers only exist in the world of ideas.

In python3, random numbers are mainly used with the random module, which generates pseudorandom numbers and is not truly random. However, Linux provides /dev/random, which can be read to obtain true random numbers from environmental noise, so this is what we use.

"True random numbers" have a different definition from "completely random numbers".

・ True random numbers are fundamentally unpredictable and truly disorderly random numbers. This is the opposite of pseudorandom numbers that are generated mathematically by a computer. Physical random numbers that use quantum behavior, such as the decay of radioactive elements, are known. True random numbers. - Shogakukan - From the Digital Daijisen.

・Perfectly random numbers refer to a sequence of numbers that occur in a completely random order, and are also called ideal random numbers. They can only be handled probabilistically. - Search Labs | By AI.

Although the definitions are different, in practice, true random numbers can be considered to be perfect random numbers and treated the same way.

Perfectly random numbers have Jungian synchronicity (a strange coincidence that goes beyond the law of causality), so they are difficult or impossible to create in the real world.

/dev/random returns one byte per read.

### Method description

rand(n) returns a true random number in the range of n*8-bit positive integers.

rand_f(n) will practically return a random float number in the range [0,1], but the distribution of random numbers is not continuous like real numbers, and it is not a truly random number because it involves one integer division.

randomint(k,n) will practically return a random integer number between 0 and n-1, but it is not a truly random number because it involves a remainder calculation.

```truerand.py
#!/usr/bin/python3
#
# truerand.py
# Python module that generates random numbers using true random numbers from /dev/random
#
import os
import binascii

# Function that returns n bytes of RAND_MAX
# in : n bytes long
# out: n bytes of RAND_MAX
def rand_max(n):
v=0
for i in range (0,n):
v=v*256+0xff
return(v)

# Function that returns n bytes of true random numbers
# parameter : n bytes long
# return : n bytes of positive integer random numbers
def rand(n):
f=open("/dev/random",'rb') # Open /dev/random
randomdata=f.read(n) # Read n bytes
f.close() # Close /dev/random
randomhex=binascii.hexlify(randomdata) #Convert to hexadecimal string

randomint=int(randomhex,16) #Convert to integer

return(randomint)

#
# Function that returns a real random number in [0,1) with n byte precision

# parameter: n bytes long

# return: Random number in [0,1)

#
# Note: Not a true random number because division is used

#
def rand_f(n):

return(rand(n)/rand_max(n))

#
# Function that returns a random number between 0 and k-1

# parameters: n bytes long

k integer

# return: Integer random number between 0 and (k-1)

#
# Note: Not a true random number because modulus operation is used

#
def randomint(k,n):

return(rand(n)%k)

if __name__=="__main__":

b=8

times=20
print(f"{b*8}bit positive true random integer")
for _ in range(times):
print(rand(b),end=" ")

print("")
print("Real random numbers in the range [0,1]")
for _ in range(times):
print(rand_f(b),end=" ")
print("")
print("Integer random numbers 0 to 99")
for _ in range(times):
print(randomint(100,b),end=" ")
print("")

```

# Execution results

```
$ truerand.py
64bit positive true random integer
3307504999628493041 16833230142106673071 12617132537912657723 13507463181985722647 10497082142665300591 6631042183926931135 15360962062758597424 13993642308568418315 766978283825206867 10039168542496294747 5012398474653242549 2895278196839792201 14818507220427785701 12973819612571874604 745060180634753097 3407469691878957494 16057494043478543453 17702076263089849866 6044349191818680689 18016755088876227617
Real random number in the range [0,1)
0.7974003807166161 0.41979958470339007 0.5609974574080073 0.867573227719673 0.4440622865950301 0.6675132571776963 0.6540182828071875 0.3561816976682385 0.8544635154444369 0.14384499913999788 0.6299092884789043 0.8762444099735378 0.12412862806208831 0.9767549851060453 0.7885647613995059 0.20188391849163984 0.42782772905419625 0.10491103155813546 0.8019370785707318 0.43197777323789693
Random integer between 0 and 99
70 33 45 38 39 88 79 9 90 38 36 43 5 49 74 81 56 71 31 29
$
```
