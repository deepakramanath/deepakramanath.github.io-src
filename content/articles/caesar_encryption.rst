:title: Caesar Encryption
:date: 2016-10-26 21:00:00
:modified: 2016-10-26 21:00:00
:tags: python, encryption
:category: Python Projects
:slug: Prime Caesar Encryption
:authors: Deepak Ramanath
:summary: A simple **encryption** is carried out over a string using **Caesar encryption method in Python**. Click **Continue reading** to know more.

Caesar encryption using Python
##############################

This project can be found at the `GitHub <https://github.com/deepakramanath/Python-Caesar-Encryption>`_ repository, including the `IPython <http://nbviewer.jupyter.org/github/deepakramanath/Python-Caesar-Encryption/blob/master/Python-Caesar-encryption.ipynb>`_ notebook.

In this program, we look at creating Caesar encryption for letters and numbers. A Caesar shift of 3 is used in this program. What this means is, for example, if we provide character **C**, the encrypter character would be **A**. Similarly, for **F**, the encrypted character would be **C**. More information about this simple encryption technique is `provided in this link <https://en.wikipedia.org/wiki/Caesar_cipher>`_.

.. code-block:: python

   import string
   from sys import argv, exit

Here, we import the module `string`. The `string` module has a number of constants and classes which can be used to obtain the required ASCII characters. In this case, we require lower and upper case English characters to compare the user provided string and subsequently get the index of the alphabets. For example, the index of **A** woulld be `0`, likewise, **B** and **C** would be `1` and `2` respectively.

.. code-block:: python

   baseAlphabetsLower = string.ascii_lowercase
   baseAlphabetsUpper = string.ascii_uppercase
   baseNumbers = range(0, 10)
   finalString = []

We store the upper case and lower case string constants in the two variables, `baseAlphabetsLower` and `baseAlphabetsUpper` respectively. For numbers, we use the `range` function to get a list from `0` to `9`.

.. code-block:: python

   userString =  raw_input("Enter your alphanumeric characters: ")

.. code-block:: python

   Enter your alphanumeric characters: The quick brown Fox jumps over the lazy Dog

The above line is self-explanatory where in the user input is stored in `userString` variable

.. code-block:: python

   for char in userString:
       if char == " ":
           finalString.append(char)
       else:
           if char in baseAlphabetsLower:
               charIndexLower = baseAlphabetsLower.index(char)
               finalString.append(baseAlphabetsLower[charIndexLower - 3])
           elif char in baseAlphabetsUpper:
               charIndexUpper = baseAlphabetsUpper.index(char)
               finalString.append(baseAlphabetsUpper[charIndexUpper - 3])
           else:
               numIndex = baseNumbers.index(int(char))
               finalString.append(str(baseNumbers[numIndex - 3]))

The lines shown above is where the left shift of 3 happens to every character and number the user provides. We first iterate through the characters and based on upper/lower case or number, `if` `else` statements are used to divert these apply the Caesar shift of 3 towards the left. The shifted characters are then appended to a `finalString` variable.


.. code-block:: python

   encryptedString = "".join(finalString)
   print "Your encrypted characters: ", encryptedString

.. code-block:: python

   Your encrypted characters:  Qeb nrfzh yoltk Clu grjmp lsbo qeb ixwv Ald

Finally, we join the `finalString` list to get the encrypted characters. Note this works for with and without space in the string provided by the user. We can verify the result from the `wiki link here <https://en.wikipedia.org/wiki/Caesar_cipher>`_



