library(StructuralVariantAnnotation)
library(VariantAnnotation)
getwd()
vcf.file <- "PASS_somaticSV.vcf"
vcf <- readVcf(vcf.file, "hg38")
gr <- c(breakpointRanges(vcf), breakendRanges(vcf))
gr1 <- breakpointgr2bedpe(gr)

write.table(gr1, "PASS_SV_bedpe.txt",sep = "\t", quote = F, row.names = F)


