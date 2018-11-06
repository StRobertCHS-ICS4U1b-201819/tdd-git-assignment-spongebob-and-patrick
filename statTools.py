
# Just Pass Procedure Part 2
def average(meanList):
    sum = 0.0
    for i in range(len(meanList)):
        sum += meanList[i]


    avg = sum / len(meanList)
    avg = round(avg,2)

    return avg

print (average([5,5,0]))
