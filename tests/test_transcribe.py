# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    
    # test with bad sequence (contains bases other than A, C, T, G)
    seq="ACTXAACCC"
    with pytest.raises(KeyError) as out:  
        transcribe(seq)
    assert out.type==KeyError
    
    # test with blank sequence
    seq=""
    with pytest.raises(ValueError) as out:  
        transcribe(seq)
    assert out.type==ValueError
    
    # test with None type
    seq=None
    with pytest.raises(TypeError) as out:  
        transcribe(seq)
    assert out.type==TypeError
    
    # test with good sequence
    seq="ACTGAACCC"
    out=transcribe(seq)
    assert out=="UGACUUGGG"
    
    # test lower case sequence
    seq="actgaaccc"
    out=transcribe(seq)
    assert out=="UGACUUGGG"
    
#     pass


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    
    # will have the same tests besides the good sequence test because reverse transcribe calls transcribe first
    
    # test with bad sequence (contains bases other than A, C, T, G)
    seq="ACTXAACCC"
    with pytest.raises(KeyError) as out:  
        reverse_transcribe(seq)
    assert out.type==KeyError
    
    # test with blank sequence
    seq=""
    with pytest.raises(ValueError) as out:  
        reverse_transcribe(seq)
    assert out.type==ValueError
    
    # test with None type
    seq=None
    with pytest.raises(TypeError) as out:  
        reverse_transcribe(seq)
    assert out.type==TypeError
    
    # test with good sequence
    seq="ACTGAACCC"
    out=reverse_transcribe(seq)
    assert out=="GGGUUCAGU"
    
    # test lower case sequence
    seq="actgaaccc"
    out=reverse_transcribe(seq)
    assert out=="GGGUUCAGU"

#     pass