:date: 2015-11-21 11:00:00
:modified: 2015-11-21 11:00:00
:tags: python, numpy, prime-numbers, prime-factors
:category: Python Projects
:slug: Prime Numbers
:authors: Deepak Ramanath
:summary: This post discusses generating **Prime Numbers** up to a given number `n` using **Python** and **numpy library**. Click **Continue reading** to know more.

Prime Numbers Using Python
##########################

This project can be found at the `GitHub <https://github.com/deepakramanath/Prime-numbers>`_ repository, including the `IPython <http://nbviewer.ipython.org/github/deepakramanath/Prime-numbers/blob/master/Prime-numbers.ipynb>`_ notebook.

============
Introduction
============

Here, we write a Python program to generate a list of Prime numbers up to a given number (`n`) and further evaluate the Prime factors for any given number. Although here the aim is not to develop an algorithm for `prime seive <https://en.wikipedia.org/wiki/Generating_primes>`_, rather use trial division to obtain the list. Once the Prime list is generated, `Prime factors <https://en.wikipedia.org/wiki/Prime_factor>`_ are subsequently evaluated.

.. code-block:: python
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

.. code-block:: python

   from sys import argv, exit
   import numpy as np


We fist put a doc message followed by importing few modules. Here we also import the `numpy` module so that we can be a little quick when we iterate through the sequence of numbers for the trial division as well as for estimating the prime factors.

.. code-block:: python

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


.. code-block:: python

   def factor(facNum):
       primeFactors = []
       for pN in primeNumbersArray:
           while True:
               if (facNum % pN) == 0:
                   facValue = facNum / pN
                   primeFactors.append(pN)
                   facNum = facValue
               else:
                   break

   return primeFactors


In this function, we evaluate the prime factors for any given number. In order to obtain the Prime factors, we first need a list of Prime numbers and that's what the former function does in this code. Now, in this function we basically iterate through the Prime number list and check if the user given number is divisible with a reminder of 0. If this condition is true, then a subsequent factorising is carried out while appending the factors to another list.


.. code-block:: python

   if len(argv) > 1:
       print(__doc__)
       exit(0)


Here, we check for the length of the initial arguments given for printing usage and help messages. Note that these three lines are commented out in the Ipython Notebook to avoid Ipython raising an exception as it tries to quit.

.. code-block:: python
   
   while True:
       number = raw_input("Enter the number: ")
       try:
           n = int(number)
           break
       except:
           print "Error: Enter only numbers"
           continue

.. code-block:: python
  
   Enter the number: 1000

Within the `while` loop, we prompt the user to enter the number `n` for generating the Prime numbers. The `try` and `except` will ensure that user enters only numbers.

.. code-block:: python

   primeNumbers = prime(n)
   print "List of Prime Numbers up to %d:" % (n)
   print primeNumbers
   primeNumbersArray = np.array(primeNumbers)


.. code-block:: python

   List of Prime Numbers up to 1000:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

At this point, we call the `prime` function and store the list as a `numpy` array which will be later used to find the prime factors.

.. code-block:: python

   while True:
       pFNum = raw_input("\nNow enter any other number to obtain the Prime Factors: ")
       try:
           pFNumber = int(pFNum)
           break
       except:
           print "Error: Enter only numbers"


.. code-block:: python
  
   Now enter any other number to obtain the Prime Factors: 5611


This second `while` loop is used to get the number from the user to evaluate the prime factors. Here, we provide a 8 bit semiprime so that when factorised, we get back the Prime numbes which when multiplied gives back the semiprime. This can be verified from this `link <http://asecuritysite.com/encryption/random3?val=8>`_.

Similar to the previous `while` loop it is ensured that the user enters only numbers with the `try` and `except`.

.. code-block:: python
   
   if pFNumber in primeNumbersArray:
       print "Its a Prime!"
   else:
       primeFactors = factor(pFNumber)
       if len(primeFactors) < 2:
           print ("Your Prime Numbers list is too short to obtain the prime factors", "Regenerate the Prime Numbers list")
       else:
           print "The Prime Factors for %d are:" %(pFNumber)
           print primeFactors

.. code-block:: python
   
   The Prime Factors for 5611 are:
   [31, 181]


Here, the number provided by the user to determine the Prime factor is first checked against the Prime number list. This is followed by printing the Prime factors.
