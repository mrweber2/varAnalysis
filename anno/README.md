# anno
Scripts and example data for generating refGene and PolyPhen2 annotations for variants using ANNOVAR.Recommend using full path to input data for each script. ANNOVAR documentation: http://annovar.openbioinformatics.org/en/latest/

## annotate_vars.sh
Run table_annovar.pl on multiple VCFs on Blue Waters, generating refGene and PolyPhen2 annotations. Modify variables internally.

Options:
```
QUEUE=normal

email=

nodes=1

thr=32

pbswalltime=00:20:00

QSUB_HEAD="#!/bin/bash"

SUFFIX=vcf

JOB_DIR=/full/path/to/job_dir

OUT_DIR=/full/path/to/output_dir

ANNOVAR_DIR=/full/path/to/annovar
```
