---
Title: Prime Numbers using Python
Date: 2010-12-03 10:20
Category: Python
Author: Deepak Ramanath
Summary: Generating Prime Numbers using Python
Tags: python, prime, numner, factors
---

This project can be found at the [GitHub](https://github.com/deepakramanath/Prime-numbers) repository, including the [IPython](http://nbviewer.ipython.org/github/deepakramanath/Prime-numbers/blob/master/Prime-numbers.ipynb) notebook.


Introduction
------------

Here, we write a Python program to generate a list of Prime numbers up to a given number (`n`) and further evaluate the Prime factors for any given number. Although here the aim is not to develop an algorithm for [prime seive](https://en.wikipedia.org/wiki/Generating_primes), rather use trial division to obtain the list. Once the Prime list is generated, [Prime factors](https://en.wikipedia.org/wiki/Prime_factor) are subsequently evaluated.

	:::python
	# Python program to calculate Prime numbers and subsequently Prime Factors

	"""
	Usage: Prime-numbers.py

	Generates a sequence of Prime numbers up to the given number (n)
	and also generates Prime factors for any user given number

	At prompt, enter only numbers

	Options
	-------

	-h or help      Displays this message

	"""


	from sys import argv, exit
	import numpy as np


We fist put a doc message followed by importing few modules. Here we also import the `numpy` module so that we can be a little quick when we iterate through the sequence of numbers for the trial division as well as for estimating the prime factors.


	:::python
	def prime(num):
    	    primeNumbers = []
            for i in np.arange(num+1):
                count_zero = 0
                if i >= 2:
                    value = i
                    for j in np.arange(1, value+1):
                        rem = value % j
                        if rem == 0:
                            count_zero = count_zero + 1
                            if count_zero >= 3:
                                break
                if count_zero == 2:
                    primeNumbers.append(i)

        return primeNumbers


This is the first function in our Python code which generates the Prime number list. As we see, we first iterate through a `numpy` array to check if the given number (`n`) is greater than 2. If this condition is satisfied, we again iterate up to `n`, where we carry out the trial division and check for the reminders. Any Prime number is a natural number that is divisible by 1 and itself producing no other positive divisors. This would mean that when we divide a number, `n` by a sequence of numbers from `1` to `n`, we should obtain only two zeros as reminders, one from  the number `1` and the other from `n`.

In the `prime` function above, after evaluating the reminder with each division, we keep a count of the reminders via the variable `count_zero`. Since we know that Prime numbers will have only two divisors, we break the loop as soon as we see any number having more than three  3 zero reminders. For those we have only two zero reminders, we append to the `primeNumbers` list.


