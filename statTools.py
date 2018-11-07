
# Implementing First Illegal Case: Empty String
def average(meanList):
    if (len(meanList) < 1):
        # Raises error if no data in the string
        raise ValueError("No Data Provided")


    else:
        try:
            sum = 0.0
            for i in range(len(meanList)):
                sum += meanList[i]


            avg = sum / len(meanList)
            avg = round(avg,2)

            return avg

        except:
            raise TypeError("Invalid Data Type Provided")




