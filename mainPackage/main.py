# main.py

# Name: Joshua Klingelhafer, JD Poindexter
# email: klingejh@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  11/14
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: In this assignment we used json and an API to find/print some interesting data from the API, in this case our API was from NASA.
# Brief Description of what this module does: This module calls the class to invoke the method inside of it. 
# Citations: Stack Overflow
# Anything else that's relevant:

from apiUtilitiesPackage.apiUtilities import *

if __name__ == "__main__":
    """
    Uses an API from apiUtilities.py to find some interesting data off of it. 
    """
    APIConnection.APILoader() 

