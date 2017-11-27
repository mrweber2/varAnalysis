# parse
Scripts and example data for parsing through VCFs and annotation output. Bash scripting provides a way to run over multiple samples and format final output.

## add_panther_anno.py
If you have PANTHER ontology info available, use this script to add to a gene data table.
```
python add_panther_anno.py -i input_gene_table_with_counts.tsv -j panther_list.txt -o output_name
```

## check_damage.sh
General bash script to check information on columns from ANNOVAR output. Edit internally.
```
FILES=/full/path/to/tables/*

for file in $FILES
do

	echo "$file"
	name=$(echo "$file" | sed "s/.*\///")
	awk -F "\t" '{ if($7=="MED12") print FILENAME"\t"$1"\t"$2"\t"$3"\t"$9"\t"$10 }' $file | sort | uniq >> MED12_locusInfo.txt

done
```
This example checks for instances of gene MED12 mutated, and prints information to output.

## indiv.sh
Run individual_transform.py on multiple samples and customize output. 
```
FILES=/full/path/to/tables/*

for file in $FILES
do
        name=$(echo "$file" | sed "s/.*\///")
        OUT=prefix.$name
        python /path/to/indiv_transform.py -i $file -j /path/to/gene_list.txt -o complete.$name
done
```

## indiv_transform.py
Transform parsed per-sample ANNOVAR output to a more useable table format.
```
python indiv_transform.py -i input_gene_table_with_counts.tsv -j gene_list.txt -o output_name
```

## transform_refGene_table.py
Transform parsed pooled ANNOVAR output to a more useable table format.
```
python transform_refGene_table.py -i input_gene_table_with_counts.tsv -j gene_list.txt -o output_name
```

