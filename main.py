from DNAToolkit import *
import random

# Creating a random DNA sequence for testing:
randDNASeq = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNASeq)

print(f"\nSequence: {DNAStr}\n")
print(f"[1] + Sequence Lenght: {len(DNAStr)}\n")
print(f"[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n")
print(f"[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n")