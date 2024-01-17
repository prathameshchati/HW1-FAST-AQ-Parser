# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    
    # check to make sure that the input sequence is not blank
    if len(seq)==0:
        raise ValueError("No bases in input sequence. Sequence must have at least one base pair.")
    
    # make all caps
    seq_f=seq.upper()
    
    new_seq=""
    for base in seq_f:
        if base in ALLOWED_NUC:
            new_seq+=TRANSCRIPTION_MAPPING[base] 
        else:
            raise KeyError("The only bases allowed are A, C, T, G. Please check inputted sequence.")
        
    return new_seq
    
    # pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    seq=transcribe(seq)
    seq=seq[::-1]
    return seq
    # pass