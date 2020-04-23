sequences= []
for i in range(int(input("How many sequences?"))):
    sequences.append(input("DNA sequence:").upper())
print(sequences)

illegal_character=0
for sequence in sequences:
    gc = 0
    mw = 0
    gc += (sequence.count("C") + sequence.count("G"))/len(sequence)
    for nucleotide in sequence:
        if nucleotide== "A":
            mw += 313.2
        elif nucleotide=="T":
            mw += 304.2
        elif nucleotide=="C":
            mw += 289.2
        elif nucleotide=="G":
            mw += 329.2
        else:
            illegal_character=1
            break
    if illegal_character!=0:
        print("Illegal character:", nucleotide)
        break
    print("DNA length:", len(sequence), "GC content:", gc, "DNA molecular weight:", mw)


