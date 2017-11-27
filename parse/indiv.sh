#!/bin/bash

FILES=/home/mrweber2/Romana_leiomyoma/for_MHudson/individuals/formatted*

for file in $FILES
do
	name=$(echo "$file" | sed "s/.*\///")
	OUT=indiv_anno.$name
	python ./indiv_transform.py -i $file -j ../gene_list.txt -o complete.$name
done
