from DNAToolkit import *
from utilities import colored
import random

# Creating a random DNA sequence for testing:
randDNASeq = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNASeq)

print(f"\nSequence: {colored(DNAStr)}\n")
print(f"[1] + Sequence Lenght: {len(DNAStr)}\n")
print(colored(f"[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n"))
print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n")
print(f"[4] + DNA String + Complement + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr)[::-1])} 5' [Complement]")
print(f"5' {colored(reverse_complement(DNAStr))} 3' [Rev. Complement]")