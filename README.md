This is a python module for extracting genuine random numbers.

There are two types of random numbers that can be used in computers: pseudo-random numbers with a period and statistically correct genuine random numbers. There are also “complete random numbers,” which cannot be handled by computers, but only probabilistically.

In python3, random numbers are mainly used with the random module, which generates pseudo-random numbers, not true random numbers. However, Linux provides /dev/random, which can be read to obtain true random numbers from environmental noise.

The definition of a “true random number” is different from that of a “complete random number.

A “true random number” is a random number that is unpredictable and truly random in principle. A “true random number” is a random number that is unpredictable in principle and truly chaotic, as opposed to a pseudo-random number generated arithmetically by a computer. Physical random numbers that utilize quantum behavior, such as the decay of radioactive elements, are known as “physical random numbers. True random number. - From Shogakukan - Digital Daizensen.

A complete random number is a sequence of numbers that are generated in a completely random order, and is also called an ideal random number. They can only be handled probabilistically. - By Search Labs | AI.

Although the definitions are different, for practical purposes, we can consider a true random number as a complete random number and treat it in the same way.

/dev/random returns one byte per read.

Method Description
rand(n) returns a truly random number in the range n*8 bits positive integer.

rand_f(n) returns a random number of type float of [0,1) for practical use, but the distribution of random numbers is not continuous like real numbers, and they are no longer truly random because they are divided among integers once.

randomint(k,n) returns integer random numbers from 0 to n-1 for practical use, but it is no longer a true random number because it performs a remainder calculation.

Translated with DeepL.com (free version)
