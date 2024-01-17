# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    # test with bad fasta file
    fa="tests/bad.fa"
    with pytest.raises(ValueError) as out:  
        list(FastaParser(fa))
    # assert str(out.value) == "File (tests/bad.fa) had 0 lines."  
    assert out.type==ValueError
    
    # test with blank fasta file
    fa="tests/blank.fa"
    with pytest.raises(ValueError) as out:  
        list(FastaParser(fa))
    assert out.type==ValueError
    
    # test with good fasta file which has a 100 sequences
    fa="data/test.fa"
    out=list(FastaParser(fa))
    assert len(out)==100
    
    # pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # input fastq file into FastaParser
    fq="data/test.fq"
    out=list(FastaParser(fq))
    
    # check that the first item is None
    assert out[0][0]==None
    
    # input fasta file 
    fa="data/test.fa"
    out=list(FastaParser(fa))

    # check that first item is not none
    assert out[0][0]!=None
    
#     pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # test with bad fastq file
    fq="tests/bad.fq"
    with pytest.raises(ValueError) as out:  
        list(FastqParser(fq))
    assert out.type==ValueError
    
    # test with blank fastq file
    fq="tests/blank.fq"
    with pytest.raises(ValueError) as out:  
        list(FastqParser(fq))
    assert out.type==ValueError
    
    # test with good fastq file which has a 100 sequences
    fq="data/test.fq"
    out=list(FastqParser(fq))
    assert len(out)==100    
    
#     pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
     # input fasta file into FastqParser
    fa="data/test.fa"
    out=list(FastqParser(fa))

    # check that first item is none
    assert out[0][0]==None
    
    # input fastq file
    fq="data/test.fq"
    out=list(FastqParser(fq))
    
    # check that the first item is not None
    assert out[0][0]!=None
    
#     pass