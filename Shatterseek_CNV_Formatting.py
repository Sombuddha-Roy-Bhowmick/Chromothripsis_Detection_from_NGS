import pandas as pd
import numpy as np
df = pd.read_table('ASCAT.segment.txt', comment='#',index_col=False, header=None)
df.columns=["sample", "chromosome","start", "end", "nmajor","nminor"]
df = df.drop(labels=0, axis=0)
df=df.drop("sample", axis=1)

df.insert(5, "total_cn", "")
df['total_cn'] = (df['nmajor'].astype(int) + df['nminor'].astype(int))

df=df.drop("nmajor", axis=1)
df=df.drop("nminor", axis=1)

values = [str (i) for i in range (1, 23)] + ["X"]
df= df.loc[df["chromosome"].isin (values)]

df.to_csv(r'ShatterseekCNV_format.txt', header=True, index=None, sep='\t')

