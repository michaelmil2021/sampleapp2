import pytest
from script2 import addme

def test():
    assert addme(1,1)==2
    assert addme(10,20)==30
    assert addme(10,-2)==8