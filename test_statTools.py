import pytest

from statTools import *

# Basic Test: Just Pass Procedure
def test_average_basicTest1 ():
    assert(average([1]) == 1)