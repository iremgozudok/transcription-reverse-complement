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
print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)} 5'\n'")