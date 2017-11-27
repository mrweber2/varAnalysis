#!/usr/bin/python

# Import and set up arparse for command options.

import argparse

parser = argparse.ArgumentParser(description='add_panther_anno.py')
parser.add_argument('-i',  type=str, required=True,  metavar='<str>', help="* gene_types.txt")
parser.add_argument('-j',  type=str, required=True,  metavar='<str>', help="* panther_list.txt")
parser.add_argument('-o',  type=str, required=True,  metavar='<str>', help="* Output file name")
args = parser.parse_args()
(IN, LIST, OUT) = (args.i, args.j, args.o)

##########  MAIN  ##########

def main():

    # Open input gene type file and output file.
    
    isFirst = False

    f = open(IN,'r')
    o = open(OUT,'w')

#    o.write('gene\tframeshift\tnonframeshift\tnonsynonymous\tsynonymous\tstopgain\tstoploss\tunknown\n')

    # Open panther file.

#    p = open(LIST,'r')

    for line in f:
        
        p = open(LIST,'r')

        lin = line.strip()
#        print lin
#        break
        sp = lin.split("\t")
        g = sp[0]                  
        o.write(lin)
        # For each line in the main input file.

        for row in p:

            # Split by tab, remove newline character. Initiate column variables.
            
            splt = row.strip().split("\t")
            gene = splt[0]
            ID = splt[1]
            NAME = splt[2]
            FAM = splt[3]
            CLASS = splt[4]
#            print gene, mut, count
            if gene == g:

                o.write('\t')
                o.write(NAME)
                o.write('\t')
                o.write(FAM)
                o.write('\t')
                o.write(CLASS)
                o.write('\n')

            else:
                continue
        p.close()
        o.write('\n')
    
    f.close()
    o.close()
main()
