#!/bin/bash

FILES=/home/mrweber2/Romana_leiomyoma/for_MHudson/individuals/raw_tables/pph*

for file in $FILES
do

	echo "$file"
	name=$(echo "$file" | sed "s/.*\///")
	awk -F "\t" '{ if($7=="MED12") print FILENAME"\t"$1"\t"$2"\t"$3"\t"$9"\t"$10 }' $file | sort | uniq >> MED12_locusInfo.txt

done
