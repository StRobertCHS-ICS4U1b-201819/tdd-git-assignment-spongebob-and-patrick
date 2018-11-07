import pytest

from statTools import *

# Basic Test: Just Pass Procedure
def test_average_basicTest1 ():
    assert(average([1]) == 1.0)

# Basic Test #2: Just Pass Procedure
def test_average_basicTest2 ():
    assert(average([1,3]) == 2.0)

# Illegal Case #1: Empty List
def test_average_illegalCase ():
    assert(average([]) == "Must be items in the string")



