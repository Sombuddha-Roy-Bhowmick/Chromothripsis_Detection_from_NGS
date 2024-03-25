import pandas as pd
import numpy as np
df = pd.read_table('PASS_SV_bedpe.txt', comment='#',index_col=False, header=None)
df.columns=["chrom1","start1","end1","chrom2","start2","end2","name","score","strand1","strand2"]
df = df.iloc[1:, :]

df.insert(7, "svclass", "")
df.insert(8, "A1", "")
df.insert(9, "A2", "")
df.insert(10, "A3", "")
df.insert(11, "A4", "")
df.insert(12, "A5", "")
df.insert(13, "A6", "")
df.insert(14, "A7", "")

df[['svclass','A1','A2','A3','A4','A5','A6','A7']]=df.name.str.split(":", expand=True)

df=df.drop("end1", axis=1)
df=df.drop("start2", axis=1)
df=df.drop("name", axis=1)
df=df.drop("score", axis=1)
df=df.drop("A1", axis=1)
df=df.drop("A2", axis=1)
df=df.drop("A3", axis=1)
df=df.drop("A4", axis=1)
df=df.drop("A5", axis=1)
df=df.drop("A6", axis=1)
df=df.drop("A7", axis=1)

df["svclass"] = df["svclass"].str.replace("Manta", "")
df["chrom1"] = df["chrom1"].str.replace("chr", "")
df["chrom2"] = df["chrom2"].str.replace("chr", "")

values = [str (i) for i in range (1, 23)] + ["X"]
df= df.loc [df ["chrom1"].isin (values)]
df = df.loc [df ["chrom2"].isin (values)]

df.to_csv(r'ShatterseekSV_format.txt', header=True, index=None, sep='\t')
