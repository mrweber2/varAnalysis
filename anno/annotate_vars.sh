#!/bin/bash

##########################################################
#
#      Run ANNOVAR on many vcfs in the same directory    #
#
##########################################################

## Set options for PBS

QUEUE=normal

email=mrweber2@illinois.edu

nodes=1

thr=32

pbswalltime=00:20:00

QSUB_HEAD="#!/bin/bash"

SUFFIX=vcf

JOB_DIR=/projects/sciteam/baib/Leiomyoma/Romana_Leiomyoma/run5

OUT_DIR=/scratch/sciteam/mrweber2/Leiomyoma/Romana_Leiomyoma/run5/vcfs

ANNOVAR_DIR=/projects/sciteam/baib/builds/annovar

## For each vcf in the current directory, generate and submit a qsub to run ANNOVAR on Blue Waters.

for vcf in *.vcf ; do
        echo "$QSUB_HEAD" > $vcf.qsub
        qsub1=$vcf.qsub
        echo "#PBS -N anno.$vcf" >> $qsub1
        echo "#PBS -o $OUT_DIR/logs/log.anno.$vcf.ou" >> $qsub1
        echo "#PBS -e $OUT_DIR/logs/log.anno.$vcf.er" >> $qsub1
        echo "#PBS -q $QUEUE" >> $qsub1
        echo "#PBS -m abe" >> $qsub1
        echo "#PBS -M $email" >> $qsub1
        echo "#PBS -l nodes=$nodes:ppn=$thr" >> $qsub1
        echo "#PBS -l walltime=$pbswalltime" >> $qsub1
        echo "#PBS -d /scratch/sciteam/mrweber2/Leiomyoma/Romana_Leiomyoma/run5/vcfs" >> $qsub1
        echo "#PBS -A baib" >> $qsub1
        echo "aprun -n $nodes perl $ANNOVAR_DIR/table_annovar.pl $OUT_DIR/$vcf $ANNOVAR_DIR/humandb/ -buildver hg19 -out anno.$vcf -remove -protocol refGene,cytoBand -operation g,r -nastring . --vcfinput" >> $qsub1
        echo `date`
        qsub $qsub1
done

