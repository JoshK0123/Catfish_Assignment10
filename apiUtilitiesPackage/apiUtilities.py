# apiUtilities.py

# Name: Joshua Klingelhafer, JD Poindexter
# email: klingejh@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  11/14
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: In this assignment we used json and an API to find/print some interesting data from the API, in this case our API was from NASA.
# Brief Description of what this module does: This module contains a class and inside the class is the function that loads an API request. It loads an API request and then finds certain data from the API by using [''].
# Citations: Stack Overflow
# Anything else that's relevant:

import json
import requests
import random
import csv


class APIConnection(object):
    """
    Establishes a connection to a database
    """
    def __init__(self, parsed_json):
        """
        Constructor
        """        
        self.__parsed_json = parsed_json
    def APILoader():
        """
        Gets an API, loads it and then stores it into a python dictionary
        @return Dictionary: A dictionary built from the API that is used
        """
        emptyListForRandomization = []
        
        # This request is getting the API from NASA from the dates October 23rd 2014 through November 1st 2014. The API itself is a daily image from each day, including explanations, copyrights, and more. 
        response = requests.get('https://api.nasa.gov/planetary/apod?api_key=WdrvyqdAMemaE5BUhX5iQjAbTEeafdRBZIruflXN&start_date=2014-10-23&end_date=2014-11-1')
    
        json_string = response.content
        parsed_json = json.loads(json_string)     
        for dailyImage in parsed_json:
            emptyListForRandomization.append(dailyImage)
            randomDataFromAPI = dict    
            randomDataFromAPI = random.choice(emptyListForRandomization) # Used the randomDataFromAPI to select random data (below are the criteria of the data) from a date in between the parameters of the API. 
        imageDate = randomDataFromAPI['date']
        imageTitle = randomDataFromAPI['title']
        imageExplanation = randomDataFromAPI['explanation']
        imageCopyright = randomDataFromAPI['copyright']
        imageJPGLink = randomDataFromAPI['hdurl']
        
        
