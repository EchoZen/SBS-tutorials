#Cleaning up and combining data
#Fasta file format
fasta= ['>geneX.1 ckdsjhethoucheh','GGCGCGC','>geneY.1 calentkhehoieb','AAAAGACAAA','>geneZ.1 oethueonu','ATTATATAC']
annotations= {'genex': 'protein kinase','geney': 'DNA polymerase','gene1': 'ribosomal protein'}

newFasta=[]
for i in range(len(fasta)):
    if ">" in fasta[i]:
        cleanID= fasta[i][1:].split('.')[0].lower() #removes unnecessary info, gets geneX,Y,Z

        if cleanID in annotations:
            header='>'+cleanID + ' ' + str(len(fasta[i+1]))+' nucleotides '+annotations[cleanID] #Prints the key of gene X and gene Y. There isn't annotations for gene Z
        else:
            header='>'+cleanID + ' ' + str(len(fasta[i+1]))+' nucleotides. No annotations found.'

    newFasta.append(header)
print(newFasta)
