Python Fibonacci Numbers
########################


:title: Fibonacci Numbers Using Python
:date: 2015-11-03 22:00:00
:modified: 2015-11-03 22:00:00
:tags: python, Fibonacci, Numbers
:category: Python Projects
:slug: Python Fibonacci Numbers
:authors: Deepak Ramanath
:summary: Here, we obtain a **Fibonacci Sequence** using **Python** and subsequently look at the **Golden Ratio**. Click **Continue reading** to know more.

Introduction
============

Here, we write a small Python program to obtain a Fibonacci Sequence for a given number, `n`. In this sequence, every consecutive number is a sum of previous two numbers. That is, the series should have `1, 2, 3, 5, 8, 13, 21, 34, 55` for `n = 10`. This sequence can continue as the value of `n` increases. In the Fibonacci Sequence, the ratio between any successive numbers is nearly constant which is equal to a value of `1.618`. This ratio is often referred to as the **Golden Ratio** and bigger the Fibonacci number, closer is the approximation. Detailed mathematical explanation regarding Fibonacci Sequence can be found `here <https://en.wikipedia.org/wiki/Fibonacci_number>`_.

.. code-block:: python

   # Python program to find Fibonacci sequence

   """
   Usage: Fibonacci-numbers.py

   Generates a Fibonacci sequence up to the given number (n) and
   calculates the Golden Ratio

   At prompt, enter only numbers

   Options
   -------

   -h or help      Displays this message

   """

.. code-block:: python

   from sys import argv, exit

Initially, we have a display message followed by importing the `sys` module. We then store the value of the first argument that is passed as we would require this for printing the help message.

.. code-block:: python

   def fibonacci(n):
       (Fn_1, Fn) = 0, 1
       FibonacciSequence = [Fn_1, Fn]
       goldenRatio = []
       for i in range(n-1):
           (Fn_1, Fn) = Fn, (Fn_1 + Fn)
           FibonacciSequence.append(Fn)
           goldenRatio.append(Fn/float(Fn_1))
   return FibonacciSequence, goldenRatio

We now define a `function` and initialise the first two values in the sequence, that is, Fn-1 and F_n and these are done with a value of `0` and `1` respectively. Note that we do this as a `tuple`. We further create two lists to store the Fibonacci and golden ratio numbers as we calculate them. The Fibonacci number is evaluated as `Fn, (Fn_1 + Fn)` for the range of `n-1` values within the `for loop`. The **Golden Ratio** is simply the ratio between Fn/Fn-1. We finally append both the Fibonacci and golden ratio numbers so that we could display a sequence.

.. code-block:: python

   if len(argv) > 1:
       print(__doc__)
       exit(0)

The above checks for any argument given along with the main Python script to display the help messages. In the Ipython Notebook, these three lines have been commented, else Ipython tries to exit and an exception is raised.

.. code-block:: python

   while True:
       number = raw_input("Enter the number, n to obtain the Fibonacci Sequence: ")
       try:
           num = int(number)
           if num > 100:
               print "Enter a value less or equal to 100"
               continue
               print "The number you have entered is: %d" % num
               break
       except:
           print "Error: Enter only numbers"
           continue

.. code-block:: python

   Enter the number, n to obtain the Fibonacci Sequence: 100
   The number you have entered is: 100

With this `while` loop, we basically ask the user to enter the value of `n` to obtain the Fibonacci Sequence and subsequently check whether the entered number is a numerical value or a string. If the value happens to be a string, the `while` loop makes sure the user is repeatedly asked until a numerical value is entered. Also, to note is that a hard limit is set to `n = 100`, else the Fibonacci number becomes excessively large.

.. code-block:: python

   FibonacciSequence, goldenRatio = fibonacci(num)

We now initialise the lists that would be used to store the Fibonacci and golden ratio numbers and the initial values. This is followed by calling the function. Finally, we print the sequence as follows:


.. code-block:: python

   print "\nFibonacci Sequence for the value, n = %d\n" % (num)
   print FibonacciSequence
   print "\nGolden Ratio\n"
   print goldenRatio

.. code-block:: python

   Fibonacci Sequence for the value, n = 100

   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738L, 19740274219868223167L, 31940434634990099905L, 51680708854858323072L, 83621143489848422977L, 135301852344706746049L, 218922995834555169026L, 354224848179261915075L]

   Golden Ratio

   [1.0, 2.0, 1.5, 1.6666666666666667, 1.6, 1.625, 1.6153846153846154, 1.619047619047619, 1.6176470588235294, 1.6181818181818182, 1.6179775280898876, 1.6180555555555556, 1.6180257510729614, 1.6180371352785146, 1.618032786885246, 1.618034447821682, 1.6180338134001253, 1.618034055727554, 1.6180339631667064, 1.6180339985218033, 1.618033985017358, 1.6180339901755971, 1.618033988205325, 1.618033988957902, 1.6180339886704431, 1.6180339887802426, 1.618033988738303, 1.6180339887543225, 1.6180339887482036, 1.6180339887505408, 1.6180339887496482, 1.618033988749989, 1.618033988749859, 1.6180339887499087, 1.6180339887498896, 1.618033988749897, 1.618033988749894, 1.6180339887498951, 1.6180339887498947, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.6180339887498947, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.6180339887498947, 1.6180339887498947, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.6180339887498947, 1.618033988749895, 1.618033988749895, 1.618033988749895, 1.6180339887498947, 1.6180339887498951, 1.618033988749895, 1.618033988749895, 1.6180339887498947, 1.618033988749895, 1.618033988749895]

