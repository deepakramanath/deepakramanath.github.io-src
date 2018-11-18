:date: 2015-12-08 14:00:00
:modified: 2015-12-08 14:00:00
:tags: python, JSON, OpenWeather, API
:category: Python Projects
:slug: Open Weather
:authors: Deepak Ramanath
:summary: Here **OpenWeather** API is explored to access weather information and parsing the *JSON* data using **Python**. Click **Continue reading** to know more and view the Python.

API call to OpenWeather and Parsing JSON using Python
#####################################################

This project can be found at the `GitHub <https://github.com/deepakramanath/Python-OpenWeather>`_ repository, including the `IPython <http://nbviewer.ipython.org/github/deepakramanath/Python-OpenWeather/blob/master/Python-OpenWeather.ipynb>`_ notebook.

Introduction
============

This is a Python program which uses `OpenWeather <http://openweathermap.org/>`_ API to access weather information and subsequently parse the JSON data. Note that to access the API in this exercise, you need to have a valid API key, which can be obtained from creating an account at `OpenWeather <http://openweathermap.org/>`_. With the free account, the `OpenWeather <http://openweathermap.org/>`_ allows you to have 600 API calls/10 minutes. Also note that a list of city IDs in JSON format is needed for this to work. This file is included in the github repository, otherwise it can be found at this `link <http://bulk.openweathermap.org/sample/city.list.json.gz>`_.


.. code-block:: python

   """
   Usage: Python-OpenWeather.py

   Makes API calls to OpenWeather and retrievs JSON data
   Parses JSON data using JSON library

   List of city ID in JSON format can be obtained from
   http://bulk.openweathermap.org/sample/

   Options
   _______

   -h or help  Displays this message
   """
 
.. code-block:: python

   import urllib
   import json
   import codecs


.. code-block:: python

   if len(argv) > 1:
      print(__doc__)
      exit(0)

.. code-block:: python

   def city():
       city = raw_input('Enter city name: ')
       city = city.lower()
       print "Retrieving weather information for %s ....." % city
    
   return city

.. code-block:: python

   def citysearch(city):
       listCities = []
       with codecs.open('city.list.json', 'r', encoding='utf8') as cityList:
           for cl in cityList:
               cityJSON = json.loads(cl)
               cityName = cityJSON['name']
               cityName = cityName.lower()
               if cityName == city:
                   searchCity = cityJSON
                   listCities.append(searchCity)
    
    cityList.close()
   
    print "Your search resulted in", len(listCities), "cities with the name %s" % city

    if len(listCities) > 1:
	    print "Please refine your search and choose the ID relevant to the country"
        for listCity in listCities:
	        print "Country: %s, " % listCity['country'], "ID: %s" % listCity['_id']
	cityID = raw_input("Enter the relevant ID: ")
	print "You have entered %s" % cityID

    elif len(listCities) == 1:
        cityID = listCities[0]['_id']
        print "Country:", listCities[0]['country']

    elif len(listCities) == 0:
        print "Your city does not exist"
        exit(0)

    return cityID

 
.. code-block:: python

   city = city()
   locationID = citysearch(city)

.. code-block:: python

   Enter city name: London
   Retrieving weather information for london .....
   Your search resulted in 7 cities with the name london
   Please refine your search and choose the ID relevant to the country
   Country: GB,  ID: 2643743
   Country: US,  ID: 5056033
   Country: CA,  ID: 6058560
   Country: US,  ID: 4119617
   Country: US,  ID: 4298960
   Country: US,  ID: 4517009
   Country: US,  ID: 5367815
   Enter the relevant ID: 2643743
   You have entered 2643743

.. code-block:: python

   apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
   serviceUrl = "http://api.openweathermap.org/data/2.5/weather?"
   url = serviceUrl + urllib.urlencode({'id': locationID, 'APPID': apikey})
   urlRead = urllib.urlopen(url).read()
   dataJSON = json.loads(urlRead)

After obtaining a valid API key, please replace `xxx...` with the valid one for `apikey` variable

.. code-block:: python

   temp = float(dataJSON['main']['temp']) - 273.0
   tempMax = float(dataJSON['main']['temp_max']) - 273.0
   tempMin = float(dataJSON['main']['temp_min']) - 273.0
   humidity = int(dataJSON['main']['humidity'])
   wind = dataJSON['wind']
   windSpeed = float(dataJSON['wind']['speed'])
   condition = dataJSON['weather'][0]['description']

.. code-block:: python

   print ""
   print "*******************"
   print "--Weather Summary--"
   print "*******************"
   print "Current Temperature: %.2f C" % temp
   print "Maximum Temperature: %.2f C" % tempMax
   print "Minimum Temperature: %.2f C" % tempMin
   print "Humidity: %d %%" % humidity

   if 'gust' in wind:
       windGust = float(dataJSON['wind']['gust'])
       print "Wind Gust:%s km/hr" % windGust
   else:
       print "Wind Gust: Data not available"

   print "Wind Speed: %.2f km/hr" % windSpeed
   print "Condition: %s" % condition

.. code-block:: python

   *******************
   --Weather Summary--
   *******************
   Current Temperature: 5.53 C
   Maximum Temperature: 7.15 C
   Minimum Temperature: 4.15 C
   Humidity: 81 %
   Wind Gust: Data not available
   Wind Speed: 5.10 km/hr
   Condition: Sky is Clear
