:date: 2015-10-21 19:35:00
:modified: 2015-10-21 19:35:00
:tags: python; regex; regular expressions; BOM
:category: Python Projects
:slug: Data extraction using Regular Expressions
:authors: Deepak Ramanath
:summary: We use **Regular Expressions** or **Regex** capabilities in **Python** to extract data sourced from `Bureau of Meteorology <http://www.bom.gov.au/>`_ (BOM). Click **Continue reading** to know more about this project.

Data extraction using Python Regular Expressions
################################################

This project can be found at the `GitHub <https://github.com/deepakramanath/Python-Regex-01>`_ repository, including the `IPython <http://nbviewer.ipython.org/github/deepakramanath/Python-Regex-01/blob/master/data_regex.ipynb>`_ notebook.

Introduction
============


This program uses Python's regular expression or regex capabilities to extract
information/data using Python's `re` module. To regex some meaningful
expressions, a data file containing meteorological information obtained from
Australia's `Bureau of Meteorology <http://www.bom.gov.au/>`_ (BOM). is used. A set of alpha-numerical and numerical data are extracted using Python's regex. Although note that regex is not the most efficient way to carry out this type of data analysis and interpretation. Here it is just used to show the versatility of regex and to learn using it for Python.

.. code-block:: python

   import sys
   import re
   import os
   import matplotlib.pyplot as plt


First, we do the importing business. Here, we import some basic modules in
Python such as sys and os. The two new probably are `re`, which is the regular
expression or regex module and, `matplotlib` is the Python's plotting library.

.. code-block:: python

   headerPattern = re.compile(r'(?P<pCode>[A-Za-z]+[ ]?[a-z]+),(?P<sNumber>(\w+[ ]?)+),(?P<ymd>(\w+,?){,3}),(?P<maxT>(\w+[ ]?\w+)),')


The first regex operation that we carry out is the compilation of the header
pattern in the `data.txt` file. Compiling the pattern converts to bytecode,
which is then subsequently used to search. At this stage, its ideal to look at
the `data.txt` if not already and to find the header information. As we see, the
header contains `Product code`, `Bureau of Meteorology station number`, `Year`,
`month`, `day`, etc and we try to extract all of these via the `headerPattern`
as shown above. Note that we use raw string `r` notation in Python and we also
group the regex using `( )`. Grouping regex is a useful feature when extracting
multiple information and they can be assigned with a choice of variable. For
example in the above, the `Produce code` is assigned to `pCode` and subsequently
when we search for `Product code` we can grab all the associated strings via
`pCode`. This feature will be become clear as we go further.

.. code-block:: python

   productCode = re.compile(r'(?P<pC>\w+)')
   stationNumber = re.compile(r'\w+,(?P<sN>\d+)')
   ymd = re.compile(r'\w+,\d+,(?P<year>\d+),(?P<month>\d+),(?P<day>\d+)')
   maxTemp = re.compile(r'\w+,(\d+,){,4}(?P<mT>\d+.\d+)')

The above are again the regex compiling for the actual data present in the
`data.txt` that we are interested to extract. Note the grouping and how the
variables are assigned for each of the regex.


.. code-block:: python

   monthValue = []
   dayValue = []
   maxTempValue = []

The above are the empty lists and will be used to update the relevant
information that is obtained when the regex are searched in the data file.

.. code-block:: python

   with open('data.txt', 'r') as data:
       for line in data:

           if not 'IDCJAC0010' in line:
               headerSearch = headerPattern.search(line.strip())
               print headerSearch.group('pCode')
               print headerSearch.group('sNumber')
               print headerSearch.group('ymd')
               print headerSearch.group('maxT')

           if not 'Product' in line:
               pCSearch = productCode.search(line.strip())
               sNSearch = stationNumber.search(line.strip())
               ymdSearch = ymd.search(line.strip())
               maxTempSearch = maxTemp.search(line.strip())

               month = ymdSearch.group('month')
               day = ymdSearch.group('day')
               mTemp = maxTempSearch.group('mT')

               monthValue.append(month)
               dayValue.append(day)
               maxTempValue.append(mTemp)

   Product code
   Bureau of Meteorology station number
   Year,Month,Day
   Maximum temperature


In the above piece of code, we open the `data.txt` for reading and then firstly
search the header pattern. Here, note that how we use the variables that we have
assigned such as `pCode`, `sNumber`, etc to store the search results. In a
similar fashion, we search the relevant data. After all the regexs are found,
the corresponding data are appended to the empty lists that we had before.


.. code-block:: python

   dataValues = zip(monthValue, dayValue, maxTempValue)
   print len(dataValues)

   365

Here, we basically `zip` the three important lists making `dataValues` as a
tuple.

.. code-block:: python

   janValues = dataValues[0:31]
   janDay = [x[1] for x in janValues]
   janTemp = [x[2] for x in janValues]

This is where it gets a bit interesting! In the previous step, the length of the
`dataValues` is printed as `365` which indicates a year worth of data. Now since
we are interested only in the January, which has `31` days, we create another
variable called `janValues` and slice the tuple from `0` to `31`. Note that
`janValues` is also a tuple with the `31` data sets. Next we use list
comprehension to dissect the tuple. `janValues` has three lists for every set of
data representing month, day and maximum temperature, in which the index[0]
would correspond to the first list which is month, index[1] for day and index[2]
for temperature.

.. code-block:: python

   febValues = dataValues[len(janValues)+1:len(janValues)+28]
   febDay = [x[1] for x in febValues]
   febTemp = [x[2] for x in febValues]

Similar to the month of January, we slice the `dataValues` into `28` days and
assign the day and temperature variables.

.. code-block:: python

   if janValues:
       plt.plot(janDay, janTemp)
       plt.xlabel('Days')
       plt.ylabel('Temperature [C]')
       plt.xlim(1,len(janValues))
       plt.title('Maximum temperature for the month of January, Station ID: IDCJAC0010')
       plt.show()
   else:
       print "Evaluate January values"

   if febValues:
       plt.plot(febDay,febTemp)
       plt.xlabel('Days')
       plt.ylabel('Temperature [C]')
       plt.xlim(1, len(febValues))
       plt.title('Maximum temperature for the month of Februrary, Station ID: IDCJAC0010')
       plt.show()
   else:
       print "Evaluate Februrary values"

