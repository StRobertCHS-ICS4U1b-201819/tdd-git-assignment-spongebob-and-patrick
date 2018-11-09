import pytest

from statTools import *

# Basic Test: Just Pass Procedure
def test_average_basicTest1 ():
    assert(average([1,4,7]) == 4.0)

# Basic Test #2: Just Pass Procedure
def test_average_basicTest2 ():
    assert(average([1,3,5]) == 3.0)

# Illegal Case #1: Empty List
def test_average_illegalCase ():
    with pytest.raises(ValueError) as errmsg:
        average([])
    assert("No Data Provided" == str(errmsg.value))

# Illegal Case #2: Incorrect Data Type
def test_average_illegalCaseTwo ():
    with pytest.raises(TypeError) as datamsg:
        average("Hello")
    assert ("Invalid List Provided" == str(datamsg.value))

# Illegal Case #2: Invalid items in a string
def test_average_illegalCaseThree ():
    with pytest.raises(TypeError) as datamsg:
        average(["Hello", 0.0])
    assert ("Invalid List Provided" == str(datamsg.value))

# Exhaustive Test Case
def test_average_exhaustiveCase ():
    assert (average([2,4.5,-7.3,23,-1.234,7,-2.3,-3]) == 2.83)

# Test Corner Case
def test_average_cornerCase ():
    assert(average([3.4]) == 3.4)

# Basic Test Standard Deviation: Just Pass Procedure
def test_standarDeviation_BasicTestOne ():
    assert(standardDeviation([60,56,61,68,51,53,69,54]) == 6.32)

# Basic Test Standard Deviation: Just Pass Procedure
def test_standardDeviation_BasicTestTwo ():
    assert (standardDeviation([4, 5, 6, 5, 3]) == 1.02)

# Exhaustive Testing
def test_standardDeviation_Exhaustive ():
    assert (standardDeviation([4.0, 5, 6.0, 5, 3, 2, 8.0, 0, 4, 6, 7, 8, 4.0, 5, 7, 9, 8, 6, 7, 5, 5.0, 4, 2, 1, 9, 3, 3, 4, 6, 4
 ]) == 2.25)

# Exhaustive Test Casing with Different Applicable Data Types
def test_standardDeviation_ExhaustiveTwo ():
    assert (standardDeviation([4.0, -5, 6.0, 5, 3, 27.45, 8.0, 0, 4, 6, -7.65, 8, 4.0, 5, 7, -9.0, 8, 6, 7, 5, 5.0, -4.5, -2, 1, 9, -3.9, 3, 4, 6, 4]) == 6.44)

# Illegal Test Case: Empty String
def test_standardDeviation_IllegalCaseOne ():
    with pytest.raises(ValueError) as valuemsg:
        standardDeviation([])
    assert("No Data Provided" == str(valuemsg.value))

# Illegal Test Case: Invalid Data Type
def test_standardDeviation_IllegalCaseTwo ():
    with pytest.raises(TypeError) as datamsg:
        standardDeviation(["Purple", "Reign"])
    assert ("Invalid List Provided" == str(datamsg.value))

# Corner Case: Only 1 value
def test_standardDeviation_CornerCase ():
    assert (standardDeviation([-3.4]) == 0.0)

# Basic Test Code For Mode
def test_mode_BasicTestOne ():
    assert (mode([3, 3, 5, 3]) == 3.0)

# Basic Test Code For Mode
def test_mode_BasicTestTwo ():
    assert (mode([3,3,3,4,4,4,5,5,5,5]) == 5.0)

# Exhaustive Testing with Decimal and Whole Numbers
def test_mode_ExhaustiveTesting ():
    assert (mode([-2, 1.0, 3.0, -2.0, 3.0, 5.4, -1, -2]) == -2.0)

# Unusual Testing. More than 1 Mode
def test_mode_UnusualCaseOne ():
    with pytest.raises(ValueError) as valErr:
        mode([-2, -1, 3.4, -1, -2, 5, -1, -2, 5])
    assert ("Error: More than 1 Mode" == str(valErr.value))

# Unusual Testing. More than 1 Mode
def test_mode_UnusualCaseTwo ():
    with pytest.raises(ValueError) as valErr:
        mode([0, 1, 2, 3, 4])
    assert ("Error: More than 1 Mode" == str(valErr.value))

# Testing Out of Bonds For Loop
def test_mode_CornerCaseOne ():
    assert (mode([2]) == 2.0)

# Handle Guarantee Case

def test_mode_CornerCaseTwo():
    with pytest.raises(ValueError) as valErr:
        mode([0, 4])
    assert ("Error: More than 1 Mode" == str(valErr.value))


# Dealing with Illegal Input
def test_mode_IllegalCaseOne ():
    with pytest.raises(TypeError) as datamsg:
        mode(["Purple", "Reign"])
    assert ("Invalid List Provided" == str(datamsg.value))

# Dealing with Empty List
def test_mode_illegalCaseTwo ():
    with pytest.raises(ValueError) as errmsg:
        mode([])
    assert("No Data Provided" == str(errmsg.value))

# Just Pass Procedure
def test_rangeFunction_basicTestOne ():
    assert (rangeFunction([1,4,2,8,10,9]) == 9.0 )




    


