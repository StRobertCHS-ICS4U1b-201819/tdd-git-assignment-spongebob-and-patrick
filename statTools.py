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

def mode (modeList):

    frequency = 1
    doubleOccurances = [0]
    lrgFreq = 0
    mode = 0.0
    length = (len(modeList) - 1)

    modeList.sort()

    for i in range(length):
        if modeList[i] == modeList[i + 1]:
            frequency += 1

        elif modeList[i] != modeList[i + 1]:
            if frequency > lrgFreq:
                doubleOccurances = [0]
                lrgFreq = frequency
                doubleOccurances[0] = lrgFreq
                mode = modeList[i]
                frequency = 1

            elif frequency == lrgFreq:
                doubleOccurances.append(lrgFreq)
                frequency = 1

        if (modeList[i] == modeList[i + 1]) and ((i + 1) == length):
            if frequency > lrgFreq:
                doubleOccurances = [0]
                lrgFreq = frequency
                doubleOccurances[0] = lrgFreq
                mode = modeList[i]

            elif frequency == lrgFreq:
                doubleOccurances.append(lrgFreq)


    mode = float(mode)

    if len(doubleOccurances) > 1:
        raise ValueError("Error: More than 1 Mode")

    else:
        return mode












