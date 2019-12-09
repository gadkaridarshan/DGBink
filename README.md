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
1.	Load the data file, process and output the data in the forms specified
2.	Read in, process and present the data as specified in the requirements section
3.	Demonstrate usage of list comprehension for at least one of the tasks
4.	Allow user input to run all of your script, or specific sections



### Who do I talk to? ###

* Repo owner or admin
Please contact Darshan Gadkari at ```darshan.gadkari@gmail.com```
