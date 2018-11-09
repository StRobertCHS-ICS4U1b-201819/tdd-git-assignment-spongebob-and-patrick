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
# Name:	mode
# Purpose:
# Returning The Mode of a List
#
# Author:	Nimal.S
#
# Created:	08/11/2018
#-------------------------------------------------------------------------------

def mode (modeList):
    """ The function finds the mode of a set of values

    :param modeList: (list) Gets the values of data in the list
    :return: (float) The mode of the list

    """

    # Handling Empty List
    if len(modeList) < 1:
        raise ValueError("No Data Provided")

    try:
        #Declare Variables
        frequency = 1
        doubleOccurances = [0]
        lrgFreq = 0
        mode = 0.0
        length = (len(modeList) - 1)
        modeList.sort()

        # Ask Mr.Fabroa, How to get it as Type Error
        modeList[0] / 1

        for i in range(length):

            # Check amount of times number occurs (sorted list)
            if modeList[i] == modeList[i + 1]:
                frequency += 1

            else:
                # If greater than largest frequency, it becomes mode
                if frequency > lrgFreq:

                    # Resets list so only largest frequency
                    doubleOccurances = [0]
                    lrgFreq = frequency
                    doubleOccurances[0] = lrgFreq
                    mode = modeList[i]
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
                    mode = modeList[i]

                elif frequency == lrgFreq:
                    doubleOccurances.append(lrgFreq)

        # Only value is mode
        if len(modeList) == 1:
            mode = modeList[0]
            return float(mode)

        # More than 1 mode
        if len(doubleOccurances) > 1:
            raise ValueError("Error: More than 1 Mode")

        # Guarantee Case
        elif len(modeList) == 2 and modeList[0] != modeList[1]:
            raise ValueError("Error: More than 1 Mode")

        else:
            return float(mode)

    # Invalid Data Type
    except TypeError:
        raise TypeError("Invalid List Provided")



