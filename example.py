from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
    
    fa_out=FastaParser("data/test.fa")
    fq_out=FastqParser("data/test.fq")
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    
    print("\n")
    print("TRANSCRIBED FASTA SEQUENCES", "\n")
    for seq in fa_out:
        print(f"{seq[0]}: {transcribe(seq[1])}")
    print("\n")
    
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console

    print("TRANSCRIBED FASTQ SEQUENCES", "\n")
    for seq in fq_out:
        print(f"{seq[0]}: {transcribe(seq[1])}")
    print("\n")
   
    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    
    print("\n")
    print("REVERSE TRANSCRIBED FASTA SEQUENCES", "\n")
    for seq in fa_out:
        print(f"{seq[0]}: {reverse_transcribe(seq[1])}")
    print("\n")
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console

    print("REVERSE TRANSCRIBED FASTQ SEQUENCES", "\n")
    for seq in fq_out:
        print(f"{seq[0]}: {reverse_transcribe(seq[1])}")
    print("\n")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
