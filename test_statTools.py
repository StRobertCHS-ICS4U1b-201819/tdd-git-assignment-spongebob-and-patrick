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
    assert ("Invalid Data Type Provided" == str(datamsg.value))

# Illegal Case #2: Invalid items in a string
def test_average_illegalCaseThree ():
    with pytest.raises(TypeError) as datamsg:
        average(["Hello", 0.0])
    assert ("Invalid Data Type Provided" == str(datamsg.value))

# Exhaustive Test Case
def test_average_exhaustiveCase ():
    assert (average([2,4.5,-7.3,23,-1.234,7,-2.3,-3]) == 2.83)

# Test Corner Case
def test_average_cornerCase ():
    assert(average([0]) == 0.0)

# Basic Test Case Standard Deviation: Just Pass
def test_standardDeviation_BasicTestOne ():
    assert(standardDeviation([60,56, 61, 68, 51, 53, 69, 54]) == 6.32)






