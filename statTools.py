#-------------------------------------------------------------------------------
# Name:	average
# Purpose:
# Returning the mean of values in a list
#
# Author:	Nimal.S
#
# Created:	07/11/2018
#-------------------------------------------------------------------------------

# Implementing First Illegal Case: Empty String
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


