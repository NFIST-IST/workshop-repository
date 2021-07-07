import os

files = os.listdir()
nbdata = [x.split(".")[0] for x in files if x.endswith("nbdata")]
ipynb = [x.split(".")[0] for x in files if x.endswith("ipynb")]

for nb in ipynb:
    if nb not in nbdata:
        s = f"""Title: {" ".join([x for x in nb.split("_") if x.isalpha()])}
Slug: {"_".join([x for x in nb.split("_") if x.isalpha()])}
Date: 2
Category: Workshop FC
Tags: Programação, Física,Secundário
Author: Bernardo Silva, Luís Lourenço
Series: Workshop FC
Series_index: {".".join([x for x in nb.split("_") if x.isnumeric()])}
Summary:"""
        with open(nb+".nbdata","w") as f:
            f.write(s)
