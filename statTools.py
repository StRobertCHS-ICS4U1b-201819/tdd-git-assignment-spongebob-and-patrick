#-------------------------------------------------------------------------------
# Name:	average
# Purpose:
# Returning the mean of values in a list
#
# Author:	Nimal.S
#
# Created:	07/11/2018
#-------------------------------------------------------------------------------

import math

def average(meanList):
    """ The function calculates the mean of values in a list

    :param meanList: (list) Gets the values of data in the list
    :return: (float) The mean value of the numbers in the list

    """

    # Must have items in the list
    if len(meanList) < 1:

        # Raises error if no data in the string
        raise ValueError("No Data Provided")

    else:
        try:
            # Find sum of list
            sum = 0.0
            for i in range(len(meanList)):
                sum += meanList[i]

            # Find average
            avg = sum / len(meanList)
            avg = round(avg,2)

            return avg

        # Else, error inputted
        except:
            raise TypeError("Invalid Data Type Provided")


# Basic Working Requirements
def standardDeviation(stdDevList):

    if len(stdDevList) < 1:
        raise ValueError("No Data Provided")

    # Find mean

    else:
        try:
            sum = 0.0
            variance = 0.0
            for m in range(len(stdDevList)):
                sum += stdDevList[m]

            avg = sum / len(stdDevList)

             # Find variance
            for x in range(len(stdDevList)):
                variance += math.pow((stdDevList[x] - avg), 2)

            # Find standard deviation and round to 2 decimal places
            stdDev = math.sqrt((variance/len(stdDevList)))
            stdDev = round(stdDev,2)

            return stdDev

        except:
            raise TypeError("Invalid Data Type Provided")
