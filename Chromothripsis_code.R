getwd()

d = read.delim("ShatterseekCNV_format.txt")
dd <- d
dd$total_cn[dd$total_cn == 0] <- 150000
dd$total_cn[is.na(dd$total_cn)] <- 0
library(GenomicRanges)
dd <- as(dd,"GRanges")
cov <- coverage(dd,weight = dd$total_cn)
dd1 <- as(cov,"GRanges")
dd1 <- as.data.frame(dd1)
dd1 <- dd1[dd1$score !=0,]
dd1 = dd1[,c(1,2,3,6)]
names(dd1) <- names(d)[1:4]
dd1$total_cn[dd1$total_cn == 150000] <- 0
d= dd1; rm(dd)

library(ShatterSeek)

sv <- read.delim("ShatterseekSV_format.txt")
SV_data <- SVs(chrom1=as.character(sv$chrom1), pos1=as.numeric(sv$start1),chrom2=as.character(sv$chrom2), pos2=as.numeric(sv$end2),SVtype=as.character(sv$svclass), strand1=as.character(sv$strand1),strand2=as.character(sv$strand2))
CN_data <- CNVsegs(chrom=as.character(d$chromosome),start=d$start,end=d$end,total_cn=d$total_cn)
chromothripsis <- shatterseek(SV.sample=SV_data,seg.sample=CN_data,genome="hg38")
Chromothripsis_1 <- chromothripsis@chromSummary
write.table(Chromothripsis_1, "Chromothripsis_Summary.txt",sep = "\t", quote = F, row.names = F)
