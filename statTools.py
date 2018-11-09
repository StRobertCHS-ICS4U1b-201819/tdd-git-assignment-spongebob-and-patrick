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
            raise TypeError("Invalid List Provided")



#-------------------------------------------------------------------------------
# Name:	standardDeviation
# Purpose:
# Returning Calculates the Standard Deviation (spread) of values in a list
#
# Author:	Nimal.S
#
# Created:	07/11/2018
#-------------------------------------------------------------------------------



def standardDeviation(stdDevList):
    """ The function calculates the mean of values in a list

        :param stdDevList: (list) Gets the values of data in the list
        :return: (float) The standard deviation of the values

    """


    # Must be items in the list
    if len(stdDevList) < 1:
        raise ValueError("No Data Provided")

    else:
        try:

            avg = average(stdDevList)

            variance = 0.0

            # Find variance
            for x in range(len(stdDevList)):
                variance += math.pow((stdDevList[x] - avg), 2)

            # Find standard deviation and round to 2 decimal places
            stdDev = math.sqrt((variance/len(stdDevList)))
            stdDev = round(stdDev, 2)

            return stdDev

        # Else, error inputted in the list
        except:
            raise TypeError("Invalid List Provided")



#-------------------------------------------------------------------------------
# Name:	verifyList
# Purpose:
# Make sure that the list has the correct data type
#
# Author:	Nimal.S
#
# Created:	09/11/2018
#-------------------------------------------------------------------------------

def verifyList (theList):
    """ The function make sure that the list has the correct data type

        :param theList: (list) Gets the values of data in the list
        :return: (bool) Returns true or false

        """

    # If incorrect data type, return false
    for i in range(len(theList)):
        if not (isinstance(theList[i], float)) and not (isinstance(theList[i], int)):
            return False

    return True


#-------------------------------------------------------------------------------
# Name:	mode
# Purpose:
# Returning The Mode of a List
#
# Author:	Nimal.S
#
# Created:	08/11/2018
#-------------------------------------------------------------------------------


def mode(modeList):
    """ The function finds the mode of a set of values

    :param modeList: (list) Gets the values of data in the list
    :return: (float) The mode of the list

    """

    #Declare Variables
    frequency = 1
    doubleOccurances = [0]
    lrgFreq = 0
    length = (len(modeList) - 1)
    modeList.sort()
    theMode = 0.0

    # Check if list has correct data type
    if verifyList(modeList) == False:
        raise TypeError("Invalid List Provided")

    # Handling Empty List
    elif len(modeList) < 1:
        raise ValueError("No Data Provided")

    # Only value is mode
    elif len(modeList) == 1:
        theMode = float(modeList[0])
        return float(theMode)

    # Exce
    elif len(modeList) == 2 and modeList[0] != modeList[1]:
            raise ValueError("Error: More than 1 Mode")
    else:

        for i in range(length):
            if modeList[i] == modeList[i + 1]:
                frequency += 1

            else:
                # If greater than largest frequency, it becomes mode
                if frequency > lrgFreq:

                    # Resets list so only largest frequency
                    doubleOccurances = [0]
                    lrgFreq = frequency
                    doubleOccurances[0] = lrgFreq
                    theMode = modeList[i]
                    frequency = 1

                # If same as greatest frequency, more than 1 mode
                elif frequency == lrgFreq:
                    doubleOccurances.append(lrgFreq)
                    frequency = 1

            # Exception case without going out of bonds
            if (modeList[i] == modeList[i + 1]) and ((i + 1) == length):
                if frequency > lrgFreq:
                    doubleOccurances = [0]
                    lrgFreq = frequency
                    doubleOccurances[0] = lrgFreq
                    theMode = modeList[i]

                elif frequency == lrgFreq:
                    doubleOccurances.append(lrgFreq)

        # More than 1 mode
        if len(doubleOccurances) > 1:
            raise ValueError("Error: More than 1 Mode")

        else:
            return float(theMode)

#-------------------------------------------------------------------------------
# Name:	mode
# Purpose:
# Returning The Mode of a List
#
# Author:	Nimal.S
#
# Created:	08/11/2018
#-------------------------------------------------------------------------------

def rangeFunction(rangeList):
    """ The function finds the range of a set of values

    :param rangeList: (list) Gets the values of data in the list
    :return: (float) The range of the list

    """

    # If empty list, raise exception
    if len(rangeList) < 1:
        raise ValueError("No Data Provided")

    try:
        # Sort list, then subtract largest and smallest numbers
        theRange = 0.0
        rangeList.sort()
        print (rangeList)

        theRange = rangeList[len(rangeList) - 1] - rangeList[0]

        return round(theRange, 2)

    # Else, Invalid Input
    except TypeError:
        raise TypeError("Invalid List Provided")


