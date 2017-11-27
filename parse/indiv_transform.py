#!/usr/bin/python

#####################################################################################################
#
#       Transform Table Format
#
#####################################################################################################
#                                                                                                   #
# Gene  Type    Count   |       | Gene  frameshift  nonframeshift   synonymous  nonsynonymous ...   #
# g1    frameshift      |       | g1    freq        freq            freq        freq          ...   #
# g1    nonframeshift   | --->  | g2                                                                #
# g1    synonymous      |       | g3                                                                #
# g2    frameshift      |       | gn                                                                #
#                                                                                                   #
#####################################################################################################

# Import and set up arparse for command options.

import argparse

parser = argparse.ArgumentParser(description='transform_refGene_table.py')
parser.add_argument('-i',  type=str, required=True,  metavar='<str>', help="* gene_types.bed")
parser.add_argument('-j',  type=str, required=True,  metavar='<str>', help="* gene_list.txt")
parser.add_argument('-o',  type=str, required=True,  metavar='<str>', help="* Output file name")
args = parser.parse_args()
(BED, LIST, OUT) = (args.i, args.j, args.o)

##########  MAIN  ##########

def main():

    # Open input gene type file and output file.
    
    isFirst = False

    f = open(BED,'r')
    o = open(OUT,'w')

    o.write('Gene\tD\tP\tB\tSTOPGAIN\tSTOPLOSS\tFRAMESHIFT\tNONFRAMESHIFT\tSYNONYMOUS\tNONSYNONYMOUS\tUNKNOWN\n')

    # Open genes file as a list.

    with open(LIST) as l:
        geneList = l.read().splitlines()

    # For each gene in the list...

    for g in geneList:
        
#        print g, " g"
#        isFirst = True

        # For each line in the main input file.

        array = [g,0,0,0,0,0,0,0,0,0,0]

        f = open(BED,'r')
        for line in f:

#            if isFirst:
#                isFirst = False
#                continue

            # Split by tab, remove newline character. Initiate column variables.
            
            splt = line.strip().split("\t")
            gene = splt[0]
            mut = splt[1]
            count = splt[2]
#            print gene, mut, count
            if gene == g:

                if mut == 'D':
			array[1] = count
                elif mut == 'P':
			array[2] = count
                elif mut == 'B':
                        array[3] = count
                elif mut == 'stopgain':
			array[4] = count
		elif mut == 'stoploss':
			array[5] = count
		elif mut == 'frameshift':
			array[6] = count
                elif mut == 'nonframeshift':
                        array[7] = count
                elif mut == 'synonymous':
                        array[8] = count
                elif mut == 'nonsynonymous':
                        array[9] = count
                elif mut == 'unknown':
                        array[10] = count
                else:
			continue
#            print array
#        print array

        f.close()
        o.write('\t'.join(map(str, array)))
        o.write('\n')

    o.close()
    f.close()
main()
