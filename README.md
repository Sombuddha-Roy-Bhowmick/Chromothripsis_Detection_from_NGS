# Chromothripsis_Detection
Detection of events like- Chromothripsis using the ShatterSeek tool from CNV and SV caller output files.

Install ASCAT (Allele-Specific Copy Number Analysis of Tumors), following instructions: https://github.com/VanLoo-lab/ascat

Please cite the following paper: Van Loo P, Nordgard SH, Lingjærde OC, et al. Allele-specific copy number analysis of tumors. Proc Natl Acad Sci U S A. 2010;107(39):16910-16915. doi:10.1073/pnas.1009843107

Install ShatterSeek, following instructions: https://github.com/parklab/ShatterSeek

Please cite the following paper: Cortés-Ciriano, I., Lee, J.JK., Xi, R. et al. Comprehensive analysis of chromothripsis in 2,658 human cancers using whole-genome sequencing. Nat Genet 52, 331–341 (2020). https://doi.org/10.1038/s41588-019-0576-7

Install Bioconductor software packages: StructuralVariantAnnotation 

(https://bioconductor.org/packages/release/bioc/html/StructuralVariantAnnotation.html).

# Code

Rscript SV_Modification.R

python Shatterseek_SV_Formatting.py

python Shatterseek_CNV_Formatting.py

Rscript Chromothripsis_code.R

# Description

SV_Modification.R (Converts the Structural Variant VCF file to a bedpe formatted file)

Shatterseek_SV_Formatting.py (Reformats the SV bedpe file into the desired input for ShatterSeek tool)

Shatterseek_CNV_Formatting.py (Reformats the ASCAT output- ASCAT.segment.txt into the desired input for ShatterSeek tool)

Chromothripsis_code.R (Uses the tool- ShatterSeek to detect chromothripsis events from NGS (next-generation sequencing) data)

# Output

The output file generated: Chromothripsis_Summary.txt

For further details and how to interpret the results, please visit the official github page of ShatterSeek.



