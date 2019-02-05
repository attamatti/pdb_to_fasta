#!/usr/bin/python

#read a pdb file output a fasta file with just the sequences

import sys
if len(sys.argv) != 2:
    sys.exit('USAGE: pdb_to_fasta.py <pdb file>')


file = sys.argv[1]
filename = file.split('.')[0]
lines = open(file,'r').readlines()

AAdict = {'ALA':'A','CYS':'C','ASP':'D','GLU':'E','PHE':'F','GLY':'G','HIS':'H','ILE':'I','LYS':'K','LEU':'L','MET':'M','ASN':'N','PRO':'P','GLN':'Q','ARG':'R','SER':'S','THR':'T','VAL':'V','TRP':'W','TYR':'Y'}

chains = {}
for line in lines:
    if 'ATOM' in line and line[13:15] == 'CA':
        if line[21] in chains:
            if line[17:20] in AAdict:
                chains[line[21]].append(AAdict[line[17:20]])
            else:
                chains[line[21]].append('X')
                print("Unknown AA: {0} at Chain {1} pos {2} using 'X'".format(line[17:20],line[21],line[23:26]))
        else:
            if line[17:20] in AAdict:
                chains[line[21]] = [AAdict[line[17:20]]]
            else:
                chains[line[21]] = ['X']
                print("Unknown AA: {0} at Chain {1} pos {2} using 'X'".format(line[17:20],line[21],line[23:26]))
output = open('{0}.fasta'.format(filename),'w')
for i in chains:
    output.write('>{0} Chain {1}\n'.format(filename,i))
    output.write('{0}\n'.format(''.join(chains[i])))