
              #           DNA to Protein translation

def translate(seq):
    data = {
        'ATA': 'ILE-', 'ATC': 'ILE-', 'ATT': 'ILE-', 'ATG': 'MET-',
        'ACA': 'THR-', 'ACC': 'THR-', 'ACG': 'THR-', 'ACT': 'THR-',
        'AAC': 'ASN-', 'AAT': 'ASN-', 'AAA': 'LYS-', 'AAG': 'LYS-',
        'AGC': 'SER-', 'AGT': 'SER-', 'AGA': 'ARG-', 'AGG': 'ARG-',
        'CTA': 'LEU-', 'CTC': 'LEU-', 'CTG': 'LEU-', 'CTT': 'LEU-',
        'CCA': 'PRO-', 'CCC': 'PRO-', 'CCG': 'PRO-', 'CCT': 'PRO-',
        'CAC': 'HIS-', 'CAT': 'HIS-', 'CAA': 'GLN-', 'CAG': 'GLN-',
        'CGA': 'ARG-', 'CGC': 'ARG-', 'CGG': 'ARG-', 'CGT': 'ARG-',
        'GTA': 'VAL-', 'GTC': 'VAL', 'GTG': 'VAL-', 'GTT': 'VAL-',
        'GCA': 'ALA-', 'GCC': 'ALA-', 'GCG': 'ALA-', 'GCT': 'ALA-',
        'GAC': 'ASP-', 'GAT': 'ASP-', 'GAA': 'GLU-', 'GAG': 'GLU-',
        'GGA': 'GLY-', 'GGC': 'GLY-', 'GGG': 'GLY-', 'GGT': 'GLY-',
        'TCA': 'SER-', 'TCC': 'SER-', 'TCG': 'SER-', 'TCT': 'SER-',
        'TTC': 'PHE-', 'TTT': 'PHE-', 'TTA': 'LEU-', 'TTG': 'LEU-',
        'TAC': 'TRY-', 'TAT': 'TRY-', 'TAA': '_', 'TAG': '_',
        'TGC': 'CYS-', 'TGT': 'CYS-', 'TGA': '_', 'TGG': 'TRY-', }
    protein = ''
    protein_list = []
    if len(seq)%3==0:   #checks wether the sequence has appropriate number of codons or not
        for i in range(0,len(seq),3):

            codon = seq[i:i+3]        #takes one codon

            if data[codon] != '_':       #checks wether the codon is stop codon or not

                protein += data[codon]

            if data[codon]=='_':  #if the codon is stop codon then it stops and add the protein to list and redefines protein = ' '

                protein_list.append(protein[:len(protein)-1])

                protein = ''

    return protein_list

print(translate("ATGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCAATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAAC"))


