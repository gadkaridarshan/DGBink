# ================================================ #
# Author: Darshan Gadkari
# Date: Dec 6, 2019
# Last Updated: Dec 9, 2019
# Bink's Coding Test
# ================================================ #

import pandas as pd
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
import logging
import json
from datetime import datetime
from os import path
from argparse import ArgumentParser
from timeit import default_timer

# setting up a loggers dict to ensure that duplicate
# log handlers are not created
loggers = {}


class Logger:
    """
    The Logger object for Darshan Gadkari's solution to Bink's
    coding test

    """
    def __init__(self, name='DG Solution Logger'):
        """
        __init__(self)

        Constructor

        """
        self.name = name

    def get_logger(self):
        """
        get_logger(self)

        Returns the logger object

        Returns
        -------
        logging.getLogger object
                    Logger object

        Examples
        --------
        >>> get_logger()

        """
        global loggers

        if loggers.get(self.name):
            return loggers.get(self.name)
        else:

            # Setup logging

            # create formatter to be used by multiple handlers
            formatter = logging.Formatter('%(asctime)s | '
                                          '%(pathname)s:%(lineno)d | '
                                          '%(funcName)s | '
                                          '%(levelname)s | '
                                          '%(message)s')

            # Create console / stream handler to write to Console
            stream_log_handler = StreamHandler()
            # Set log level to DEBUG
            stream_log_handler.setLevel(logging.DEBUG)
            # Set formatter to the console handler
            stream_log_handler.setFormatter(formatter)

            # Create file handler to write to a log file
            file_log_handler = RotatingFileHandler('logs/app.log',
                                                   maxBytes=10000000,
                                                   backupCount=10)
            # Set log level to DEBUG
            file_log_handler.setLevel(logging.DEBUG)
            # Set formatter to the file handler
            file_log_handler.setFormatter(formatter)

            # create logger
            logger = logging.getLogger(self.name)
            logger.setLevel(logging.DEBUG)

            # add console log handler to the logger
            logger.addHandler(stream_log_handler)

            # add file log handler to the logger
            logger.addHandler(file_log_handler)

            loggers[self.name] = logger

            # return the logger object
            return logger


class Solution:
    """
    The Solution is for Darshan Gadkari's solution to Bink's
    coding test

    Attributes
    ----------
    logger 	: logging.getLogger
                logger object to log to console
    df 		: pandas.DataFrame
                DataFrame to be used throughout the solution

    """
    def __init__(self, data_file='data/Python Developer Test Dataset NEW.csv'):
        """
        __init__(self, data_file='data/Python Developer Test Dataset NEW.csv')

        Constructor

        Parameters
        ----------
        data_file : str
                    Name and the relative path of the data file
                    Default value: 'data/Python Developer Test Dataset NEW.csv'

        """
        # get the logger object
        self.logger = Logger().get_logger()

        # Requirement 1 (because it will be required as a
        # precursor to all other requirements:
        #     read the data file into a pandas DataFrame
        self.df = self.read_file(data_file=data_file)
        self.logger.info(f'Shape of the dataframe: {self.df.shape}')

    def execute_all_requirements(self):
        """
        execute_all_requirements(self, data_file)

        Execute  the requirements

        Examples
        --------
        >>> execute_all_requirements()

        """

        # Action 4:
        #     Allow user input to run all of your script, or specific sections

        # Requirement 1
        self.requirement_1()

        # Requirement 2
        self.requirement_2()

        # Requirement 3
        self.requirement_3()

        # Requirement 4
        self.requirement_4()

    def requirement_1(self):
        """
        requirement_1(self)

        Executes requirement 1

        Examples
        --------
        >>> requirement_1()

        """

        # Action 4:
        #     Allow user input to run all of your script, or specific sections

        # Requirement 1.a:
        #     Produce a list sorted by “Current Rent” in ascending order
        # Requirement 1.b:
        #     Obtain the first 5 items from the resultant list
        #     and output to the console
        df_requirement = self.df_rent_sorted_asc[:5]
        self.logger.info('First five items of sorted in '
                         'ascending order of Current Rents:\n{0}'.
                         format(df_requirement))
        return df_requirement

    def requirement_2(self):
        """
        requirement_2(self)

        Executes requirement 2

        Examples
        --------
        >>> requirement_2()

        """

        # Action 4:
        #     Allow user input to run all of your script, or specific sections

        # Requirement 2:
        #     From the list of all mast data, create a new list
        #     of mast data with “Lease Years” = 25 years
        # Requirement 2.a:
        #     Output the list to the console, including all data fields
        df_requirement = self.df_lease_years_25
        self.logger.info('List of mast data '
                         'with "Lease Years" = 25:\n{0}'.
                         format(self.df_lease_years_25))

        # Requirement 2.b:
        #     Output the total rent for all items in this list to the console
        total_rent = self.df_lease_years_25['Current Rent'].sum()
        self.logger.info('Total rent of all items '
                         'with "Lease Years" = 25: {0:.2f}'.
                         format(total_rent))

        return df_requirement, total_rent

    def requirement_3(self):
        """
        requirement_3(self)

        Executes requirement 3

        Examples
        --------
        >>> requirement_3()

        """

        # Action 4:
        #     Allow user input to run all of your script, or specific sections

        # Requirement 3:
        #     Create a dictionary containing tenant name
        #     and a count of masts for each tenant
        self.df_groupby_tenant_name = self.df.\
            groupby(['Tenant Name']).size().astype(str)

        # Requirement 3.a:
        #     Output the dictionary to the console in a readable form
        output_dict = self.df_groupby_tenant_name.to_dict()
        output_dict_as_string = json.dumps(output_dict, indent=4)
        self.logger.info('dictionary containing tenant name '
                         'and a count of masts for each tenant:\n{}'.
                         format(output_dict_as_string))
        return output_dict_as_string, output_dict

    def requirement_4(self):
        """
        requirement_4(self)

        Executes requirement 4

        Examples
        --------
        >>> requirement_4()

        """

        # Action 4:
        #     Allow user input to run all of your script, or specific sections

        # Requirement 4:
        #     List the data for rentals with “Lease Start Date”
        #     between 1st June 1999 and 31st August 2007
        # Requirement 4.a:
        #     Output the data to the console with dates
        #     formatted as DD/MM/YYYY
        df_requirement = self.df_lease_start_date_between_range
        self.logger.info('List of mast data '
                         'with "Lease Start Date" between 1st June 1999 '
                         'and 31st August 2007 = \n{}'.
                         format(df_requirement))
        return df_requirement

    def read_file(self, data_file):
        """
        read_file(self, data_file)

        Reads the file provided as an argument

        Parameters
        ----------
        data_file : str
                    Name and the relative path of the data file

        Returns
        -------
        Pandas DataFrame
                    DataFrame created from reading the Data file

        Examples
        --------
        >>> read_file(data_file='data/Python Developer Test Dataset NEW.csv')

        """
        self.logger.info('About to read the data file')

        # Action 3:
        #     Demonstrate usage of list comprehension for at
        #     least one of the tasks
        # if file exists then read it into a DataFrame and return
        #     it
        # else return an empty DataFrame
        return pd.read_csv(data_file) \
            if path.exists(data_file) \
            else pd.DataFrame()

    @property
    def df_rent_sorted_asc(self, list_of_columns=['Current Rent'],
                           ascending=True):
        """
        df_rent_sorted_asc(self)

        Sorts the DataFrame based on the provided column(s)

        Parameters
        ----------
        list_of_columns : list
                    list of columns to sort by
        ascending       : bool
                    True of ascending else False

        Returns
        -------
        Pandas DataFrame
                    DataFrame created from reading the Data file

        Examples
        --------
        >>> df_rent_sorted_asc()

        """
        return self.df.sort_values(by=list_of_columns, ascending=ascending)

    @property
    def df_lease_years_25(self):
        """
        df_lease_years_25(self)

        Slices the DataFrame based on “Lease Years” = 25

        Returns
        -------
        Pandas DataFrame
                    Sliced DataFrame

        Examples
        --------
        >>> df_lease_years_25()

        """
        return self.df[self.df['Lease Years'] == 25]

    @property
    def df_lease_start_date_between_range(self):
        """
        df_lease_start_date_between_range(self)

        Slices the DataFrame based on date range
        and formats the Lease Start Date column

        Returns
        -------
        Pandas DataFrame
                    Sliced DataFrame with formatted column

        Examples
        --------
        >>> df_lease_start_date_between_range()

        """
        self.df['Lease Start Date'] = pd.\
            to_datetime(self.df['Lease Start Date'])
        df_output = self.df[(self.df['Lease Start Date']
                            >= datetime(1999, 6, 1, 0, 0)) &
                            (self.df['Lease Start Date'] <
                                datetime(2007, 9, 1, 0, 0))].copy()
        df_output.loc[:, 'Lease Start Date'] = df_output['Lease Start Date'].\
            dt.strftime('%d/%m/%Y')
        return df_output


if __name__ == "__main__":
    parser = ArgumentParser()
    # set up -r or --requirement as a argument
    # default value = all which implies execute for all
    # requirements
    req = parser.add_argument(
        "-r",
        "--requirement",
        type=str,
        choices=['1', '2', '3', '4', 'all'],
        help="the type of requirement [1|2|3|4|all",
        default='all')
    args = parser.parse_args()

    if args.requirement == 'all':
        solution = Solution()
        solution.execute_all_requirements()
    elif args.requirement == '1':
        solution_1 = Solution()
        solution_1.requirement_1()
    elif args.requirement == '2':
        solution_2 = Solution()
        solution_2.requirement_2()
    elif args.requirement == '3':
        solution_3 = Solution()
        solution_3.requirement_3()
    elif args.requirement == '4':
        solution_4 = Solution()
        solution_4.requirement_4()
