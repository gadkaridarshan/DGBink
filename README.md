# DGBink
DG solution to Bink test

``` 
# ================================================ #
# Author: Darshan Gadkari
# Date: Dec 6, 2019
# Bink's Coding Test
# ================================================ #
```

### What is this repository for? ###

* Quick summary
This is a benchmark test to ensure that Darshan Gadkari can show a good understanding of the fundamentals of reading, coding and delivering to a timeframe.

* Version
v1.0.0

* Link to repo


### How do I get set up? ###

* Summary of set up

1. Please install Python 3.6.*. If you have conda or virtualenv or venv, please create 
an environment with Python 3.6.x. I have used conda
1.1. To create an environment in conda: ```conda create -n py36 python=3.6```

2. If you use a virtual environment, please activate that environment
2.1 To activate conda environment named, py36: ```source activate py36```


* Configuration and Dependencies

Please install the requirements from requirements.txt
```
cd DGBink
pip install -r requirements.txt
```

* How to run tests
Please use pytest. Alternatively you can use unittest or other testing packages
but this repo is tested with pytest
```
cd DGBink
pytest -v
pytest -vs (to print console logs while testing)
```

* Actions of the test

A data file will be provided alongside this test. The dataset is a CSV which contains publicly available data about mobile phone masts in an area of the UK. This file contains un-normalised data (such as multiple variations of Tenant Name) – treat these as individual tenants.

Actions
1.	Load the data file, process and output the data in the forms specified - DONE
2.	Read in, process and present the data as specified in the requirements section - DONE
3.	Demonstrate usage of list comprehension for at least one of the tasks - DONE
4.	Allow user input to run all of your script, or specific sections - DONE

* Code Requirements

1.	Read in the attached file - DONE
a.	Produce a list sorted by “Current Rent” in ascending order - DONE
b.	Obtain the first 5 items from the resultant list and output to the console - DONE
2.	From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years. - DONE
a.	Output the list to the console, including all data fields - DONE
b.	Output the total rent for all items in this list to the console - DONE
3.	Create a dictionary containing tenant name and a count of masts for each tenant - DONE
a.	Output the dictionary to the console in a readable form - DONE
4.	List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007 - DONE
a.	Output the data to the console with dates formatted as DD/MM/YYYY - DONE

To run all requirements
```
cd DGBink
python solution.py --requirement all

```

To run requirement 1
```
cd DGBink
python solution.py --requirement 1

```

To run requirement 2
```
cd DGBink
python solution.py --requirement 2

```

To run requirement 3
```
cd DGBink
python solution.py --requirement 3

```

To run requirement 4
```
cd DGBink
python solution.py --requirement 4

```

* Going above and beyond
1. Implemented Logger class
1.1. Ensured that if duplicate log handlers are not created
2. Docstrings numpy style
3. Set up some class methods for their use as properties instead of methods
4. Implement File Logging in addition to Console Logging


### Who do I talk to? ###

* Repo owner or admin
Please contact Darshan Gadkari at ```darshan.gadkari@gmail.com```
